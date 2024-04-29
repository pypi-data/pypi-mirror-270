#!/usr/bin/env python3

"""Package for adding a quantity-aware quantity_text_input field to Streamlit pages."""

import re
from decimal import Decimal
from typing import Union
import streamlit as st
import pint

__author__ = "Holger Døssing (hldn@novonordisk.com)"
__license__ = "MIT"
__version__ = "0.1.0a"


def ureg(expression: str) -> pint.Quantity:
    """Returns a pint.UnitRegistry instance with necessary parameters.
    (Note: We use a singleton pattern, because we *must* use the same pint.UnitRegistry everywhere.
    This is necessary because pint cannot compare Quantities created with different registry instances
    - it raises a ValueError ("Cannot operate with Quantity and Quantity of different registries."
    By putting ureg() in root scope, it will be shared by all quantity_text_input fields on a page.) 
    """
    try:
        ureg.singleton  # (function properties can be used as static vars)
    except AttributeError:
        ureg.singleton = pint.UnitRegistry(
            autoconvert_offset_to_baseunit = True,  # for handling offset temperatures (*C, *F)
            non_int_type=Decimal,   # use Decimal for all non-integer numbers
            )
        ureg.singleton.default_format = "f~P"  # f = fixed-point (suppresses scientific notation), ~ = shortest unit prefix, P = pretty print
    return ureg.singleton(expression)


def quantity_text_input(
        label: str,
        preprocessor: callable = None,
        relaxed_temperature_parsing: bool = True,
        equate_mw_and_molar_mass: bool = True,
        mandatory: bool = False,
        mandatory_dimension: str = None,
        lower_limit: str = None,
        upper_limit: str = None,
        output_unit: str = None,
        **kwargs,
        ) -> pint.Quantity:
    """Inserts a streamlit text_input field for inputting a quantity.
    The input will be parsed by the pint library and returned as a pint.Quantity object
    whose magnitude is a Decimal instance.
    A typical input will be in the format "{number} {unit}" (e.g. "25.3 nanogallons"),
    but "1/3 cup" or "1.5e3 uM" are also valid inputs.
    If the input cannot be parsed or is invalid, an error message will be displayed below
    the input field to alert the user.

    The input field inherits all arguments from Streamlit's st.text_input.
    In addition, the following optional arguments are also available:

    - preprocessor:             A callable that takes the user's input as a string and returns
                                a string. Use this to preprocess the input before it is
                                parsed by the quantity_text_input field.
                                Return a blank string (or None) to reject the input.
                                Useful for e.g. stripping (and storing) non-quantity metadata
                                from the user's input before parsing the remainder into a quantity.

    - relaxed_temperature_parsing: If True, generalizes typical (but incorrect) temperature
                                inputs to sth that the pint library can parse properly.
                                Disable this if you want to be able to parse units of
                                Coulombs (C), Fahrads (F), angular degrees (°), and the molar
                                gas constant (R), as these will otherwise be converted to
                                Celsius, Fahrenheit, or Rankine.

    - equate_mw_and_molar_mass: If True, automatically 'converts' Da to g/mol and vice
                                versa when the user is asked to input one but provides the other.
                                This false equality is commonly used among molecular biologists.

    - mandatory:                If True, an error message will be shown to the user, if the input
                                field is empty.
                                Consider adding e.g. an asterisk (*) to the label to indicate
                                that the field is mandatory.

    - mandatory_dimension:      Only accept inputs of the specified physical dimension (the user
                                is still free to use whatever unit and/or prefix they like, though).
                                Valid dimensions are:
                                "mass",
                                "volume",
                                "substance amount" (i.e. mol, molecules etc.),
                                "molarity" (i.e. particles/gallon etc.),
                                "mass concentration" (i.e. g/l, stone/floz etc.),
                                "molar mass" (i.e. g/mol, lbs/cc etc.),
                                "molecular weight" (i.e. Da, amu),
                                "duration".
                                (Note: Entering durations can be tricky for users, as the pint library
                                accepts many different units for time. Consider using a preprocessor
                                to standardize time inputs.)

    - lower_limit:              Both the user's input and the given lower_limit string will
                                be parsed as pint.Quantity objects. If the user's input is
                                less than lower_limit an error message will be shown.
                                (The pint library will handle the unit-aware comparison of the
                                two quantities.)
                                Please note that the lower_limit must be of the same dimension as
                                the user's input. Hence, it is *strongly* recommended that the
                                enforced_quantity_dimension argument is used in conjunction with
                                lower_limit.

    - upper_limit:              Works similar to lower_limit.

    - output_unit:              Format the output pint.Quantity object to the given unit, e.g.
                                microliters.
                                Please note that the output_unit must be of the same dimension as
                                the user's input. Hence, it is *strongly* recommended that the
                                enforced_quantity_dimension argument is used in conjunction with
                                output_unit.
    """


    class QuantityTextInputException(Exception):
        """Base exception for quantity_text_input-related issues."""

    class QuantityTextInputMismatch(QuantityTextInputException):
        """Raised when there is a mismatch between two quantities' dimensions."""

    class QuantityTextInputTypeError(QuantityTextInputException):
        """Raised when a parameter is of the wrong type."""

    class QuantityTextInputUnitError(QuantityTextInputException):
        """Raised when there is an issue with a unit in the input string."""

    class QuantityDimension:
        """Class for tying a pint unit string and a human-readable description to a moniker."""

        def __init__(self, input_string: str):
            """Look up the list of known quantity dimensions and return a QuantityDimension
            object with the corresponding description and pint syntax of the dimension.
            The input string can be either a dimensionality moniker (e.g. "mass") or a quantity (e.g. "1 kg").
            If the input is blank/None, None is returned.
            """
            if input_string:
                try:  # look up the input string in the list of known dimensions
                    _description, _quantity_string = {
                        # shorthand: (description, example unit)
                        "number":             ("unitless number", ""),
                        "mass":               ("mass", "g"),
                        "volume":             ("volume", "l"),
                        "duration":           ("duration", "s"),
                        "temperature":        ("temperature", "degC"),
                        "substance amount":   ("substance amount (number of moles)", "mol"),  # pint also accepts 'molecules' as a unit here
                        # concentrations
                        "molarity":           ("molarity (mol/l)", "M"),  # pint also accepts moles per any-other-volume-unit
                        "mass concentration": ("mass concentration (e.g. g/l)", "g/l"),  # pint also accepts 'stone/floz' etc.
                        # molecules and bulk
                        "molecular weight":   ("molecular weight (Da)", "Da"),
                        "molar mass":         ("molar mass (g/mol)", "g/mol"),
                    }[input_string]
                except KeyError:
                    # assume the input is a quantity string
                    _description = input_string
                    _quantity_string = input_string

                try:  # try to parse as a pint.Quantity object
                    self.description = _description
                    self._quantity = ureg(_quantity_string)
                except:  # okay, that didnt' work, let's just synthesise a description and dimensionality
                    raise QuantityTextInputException(f"Error while parsing '{input_string}' as a QuantityDimension object.")
            
        def __bool__(self):
            """Return False if instance is invalid."""
            return hasattr(self, "description") and hasattr(self, "_quantity")
        
        def __lt__(self, other: "QuantityDimension"):
            return self._quantity < other._quantity
            
        def __str__(self):
            return self.description
        
        def check(self, other: Union[pint.Quantity, "QuantityDimension"]) -> bool:
            """Check if the given object's dimensionality matches self's dimensionality"""
            if isinstance(other, pint.Quantity):
                return other.check(self._quantity)
            elif isinstance(other, QuantityDimension):
                return other._quantity.check(self._quantity)
        

    def validate_parameters() -> None:
        """Validates the validity and (when relevant) internal inter-compatibility of all quantity_text_input()-specific
        parameters. If needed, raises an exception with a descriptive error message.
        This is mainly intended as a developer tool to catch errors in the use of the quantity_text_input() function.
        """
                       
        def assert_numeric(var_name: str, var_value: any) -> None:
            if var_value:
                try:
                    assert re.search(r"\d", var_value)
                except:
                    raise QuantityTextInputTypeError(f"""Parameter issue: Parameter {var_name} must contain a number, but given value '{var_value}' does not.""") from None
                
        def assert_callable(var_name: str, var: any) -> None:
            if var:
                if not callable(var):
                    raise QuantityTextInputTypeError(f"""Parameter issue: Parameter {var_name} must be a callable or None, but given value '{var}' is {type(var)}.""")
                
        def assert_dimensional(var_name: str, var: any) -> QuantityDimension:
            if var:
                try:
                    QuantityDimension(var)
                except Exception as err:
                    raise QuantityTextInputException(f"""Parameter issue: Error while parsing {var_name} ('{var}'): {err}""") from None

        def assert_quantity(var_name: str, var: any) -> pint.UnitRegistry:
            if var:
                try:
                    to_quantity(var)
                except pint.errors.UndefinedUnitError as err:
                    raise QuantityTextInputUnitError(f"""Parameter issue: Unknown unit '{err.unit_names}' for parameter {var_name}.""")
                except pint.errors.DimensionalityError:
                    raise QuantityTextInputUnitError(f"""Parameter issue: Dimensionality error while parsing {var_name}: '{var}'.""")
                except Exception as err:
                    raise QuantityTextInputException(f"""Parameter issue: Error while parsing {var_name} ('{var}'): {err}""")
                
        def assert_common_dimensionality(var1_name: str, var1: any, var2_name: str, var2: any) -> None:
            if var1 and var2:
                obj1 = QuantityDimension(var1)
                obj2 = QuantityDimension(var2)
                if obj1 and obj2 and not obj1.check(obj2):
                    raise QuantityTextInputMismatch(f"""Parameter issue: Dimensionality mismatch between {var1_name} ('{obj1}') and {var2_name} dimension ('{obj2}').""")

        assert_callable("preprocessor", preprocessor)
        assert_dimensional("mandatory_dimension", mandatory_dimension)
        assert_numeric("lower_limit", lower_limit)
        assert_numeric("upper_limit", upper_limit)
        assert_quantity("lower_limit", lower_limit)
        assert_quantity("upper_limit", upper_limit)
        assert_quantity("output_unit", output_unit)

        if (lower_limit or upper_limit or output_unit) and not mandatory_dimension:
            raise QuantityTextInputException("Parameter issue: The 'mandatory_dimension' parameter must be set if 'lower_limit', 'upper_limit', or 'output_unit' is set.")

        assert_common_dimensionality("mandatory_dimension", mandatory_dimension, "output_unit", output_unit)
        assert_common_dimensionality("mandatory_dimension", mandatory_dimension, "lower_limit", lower_limit)
        assert_common_dimensionality("mandatory_dimension", mandatory_dimension, "upper_limit", upper_limit)

        if lower_limit and upper_limit:
            if not QuantityDimension(lower_limit) < QuantityDimension(upper_limit):
                raise QuantityTextInputException(f"""Parameter issue: The lower_limit ('{lower_limit}') must be smaller than upper_limit ('{upper_limit}').""")


    def warn(error_message: str):
        """Displays any warnings to the user re. their input in the Streamlit app.
        Warnings are shown in an st.empty() container below the input field.
        ---
        Note: Error messages/warnings should not merely tell what the error *is*,
        but instead they should convey to the user *how* they may correct the error.
        """
        with st.empty():
            st.error(error_message)


    def preparse_maths_and_numbers(s: str) -> str:
        """Converts multiplication signs ('x' and '×'), converts fractions and
        mixed numbers (e.g. 2⅓) to sth that the pint library can parse properly.
        Returns None and warns the user if the input contains math traps that
        cannot be resolved automatically.
        """
        # replace multiplication signs 'x' and '×' (e.g. '2x10^3' -> '2*10^3')
        s = re.sub(r"(\d|\S\s)[x×](\d|\s\S)", r"\1 * \2", s)
        # replace '½' glyph with fraction
        s = re.sub(r"(?<=[\d\b])(½)", r".5 ", s)
        # fix mixed numbers (e.g. '19 2/3' -> '(19 + (2/3)) ')
        s = re.sub(r"(?<![/\.])(\b\d+)\s+(\d+/\d+)(?!/)", r"(\1+(\2)) ", s)
        # any whitespace between digits may trigger some under-the-hood automagical
        # pint maths that the user won't necessarily realise, so reject the input
        # (the user can fix their input by adding brackets and/or operators, like * or +)
        if re.search(r"[\d)]\s+\.?\d", s):  # (still doesn't catch '2 liter 6', though)
            warn("Number parsing error. Please reword your input.")
            return None
        return s.strip()


    def preparse_temperatures(s: str) -> str:
        """Fixes a bunch of common issues with temperature inputs and returns
        a string of the format 'x °C', 'x °F', 'x °R', or 'x K' (where x is a number),
        which pint can parse.
        (Note, however, that this compromises the ability to parse Coulombs 'C',
        Fahrads 'F', the molar gas constant 'R', and angular degrees '°').
        """
        # a few regex test cases:
        """ 1°, 2°celsius, 3°Celsius, 4 °C, 5 °celsius, 6 °Celsius, 7 °F, 8 °Fahrenheit,
            9 °fahrenheit, 10*, 11*C, 12 *C, 13 *celsius, 14C, 15F, 16K, 17 K, 18.1*C, 19.12*,
            20 degrees, 21 degrees C, 22 degree, 25 C, 26 F, 27 K
        """
        # special case: input is 'C' or 'F' only (happens when output unit is 'C' or 'F')
        s = f"0 {s}" if s == "C" or s == "F" else s
        # replace 'degrees', 'degree', and '*' with '°' (degree symbol)
        s = re.sub(r"(\d*\.?\d+)\s?(degrees|degree|\*(?=C\b|F\b|R\b))", r"\1 °", s)
        # substitutions
        s = re.sub("celsius", "C", s, flags=re.IGNORECASE)
        s = re.sub("fahrenheit", "F", s, flags=re.IGNORECASE)
        s = re.sub("kelvin", "K", s, flags=re.IGNORECASE)
        s = re.sub("rankine", "R", s, flags=re.IGNORECASE)
        s = re.sub("degC", "°C", s, flags=re.IGNORECASE)
        s = re.sub("degF", "°F", s, flags=re.IGNORECASE)
        s = re.sub("degR", "°R", s, flags=re.IGNORECASE)
        s = re.sub("degK", "K", s, flags=re.IGNORECASE)
        # remove whitespace between '°' and 'C', 'F', or 'R' (e.g. '37 ° C' -> '37 °C'),
        # and also add a degree symbol if missing
        s = re.sub(r"(\d*\.?\d+)\s?°?\s+(C|F|R)\b", r"\1 °\2", s)
        return s.strip()
    

    def is_input_blank(input_string: str) -> bool:
        """Returns True if the given string is blank (or whitespace only).
        If input is mandatory (mandatory=True), the user is warned accordingly.
        """
        if input_string.strip() == "":
            if mandatory:
                if mandatory_dimension:
                    _description = QuantityDimension(mandatory_dimension).description
                    warn(f"{_description[:1].upper() + _description[1:]} required.")
                else:
                    warn(f"Quantity required.")
        return not bool(input_string)
        
        
    def to_quantity(input_string: str) -> pint.Quantity:
        """Parses freetext representing a quantity into a pint.Quantity object."""
        if input_string:
            input_string = preparse_maths_and_numbers(input_string)
        if input_string:  # check again; preparsing may have returned an empty string
            if relaxed_temperature_parsing:
                input_string = preparse_temperatures(input_string)
        if input_string:  # check again; preparsing may have returned an empty string
            quantity = ureg(input_string)
            return quantity
        

    def parse_input_to_quantity(input_string: str) -> pint.Quantity:
        """Parse freetext representing a quantity into a pint.Quantity object.
        If the user gave us an unparsable string, we warn them.
        """
        try:
            return to_quantity(input_string)
        except pint.errors.UndefinedUnitError as err:
            warn(f"Unknown unit '{err.unit_names}'.")
            return None
        except pint.errors.DimensionalityError:
            warn("Parsing error. Please reword your input.")
            return None
        except Exception:
            warn("Parsing error. Please reword your input.")
            return None
                

    def normalize_mw_and_molar_mass(_quantity: pint.Quantity) -> pint.Quantity:
        """If the user is asked to input a molecular weight (Da)* but provided
        a molar mass (g/mol)*, or vice versa, we convert the input to the requested
        dimension, using the molecular biologist's rule-of-thumb: 1 Da = 1 g/mol.
        (* or similar units of mass or mass-per-amount.)
        """
        if equate_mw_and_molar_mass:
            try:
                if QuantityDimension(mandatory_dimension) == QuantityDimension("molar mass") and _quantity.check(QuantityDimension("molecular weight")):
                    _quantity = ureg(f"{_quantity.to('Da').magnitude} g/mol")  # asked for g/mol; convert from Da
                elif QuantityDimension(mandatory_dimension) == QuantityDimension("molecular weight") and _quantity.check(QuantityDimension("molar mass")):
                    _quantity = ureg(f"{_quantity.to('g/mol').magnitude} Da")  # asked for Da; convert from g/mol
            except Exception:
                print(f"Warning: Unable to perform interconversion between molecular weight and molar mass for '{_quantity}'. Returning it as-is.")
        return _quantity


    def is_quantity_of_mandatory_dimension(_quantity: pint.Quantity) -> bool:
        """Return True if the user's input (converted to a Quantity) is of 
        the expected dimension, else display a warning and return False.
        """
        if mandatory_dimension:
            _mandatory_dimension = QuantityDimension(mandatory_dimension)
            _quantity = normalize_mw_and_molar_mass(_quantity)  # special case: molecular biologists often equate Da with g/mol            
            try:
                if not _mandatory_dimension.check(_quantity):
                    warn(f"Must be a {_mandatory_dimension}.")
                    return False
            except AttributeError:
                warn(f"Missing {_mandatory_dimension} unit.")
                return False
        return True


    def is_quantity_within_limits(_quantity: pint.Quantity) -> bool:
        """Return True if the user's input is within the stated limits,
        else display a warning and return False.
        """
        if lower_limit:
            _lower_limit = to_quantity(lower_limit)
            if _quantity < _lower_limit:
                warn(f"Must be ≥ {_lower_limit}.")
                return False
        if upper_limit:
            _upper_limit = to_quantity(upper_limit)
            if _quantity > _upper_limit:
                warn(f"Must be ≤ {_upper_limit}.")
                return False
        return True
    

    def process_input(input_string: str) -> pint.Quantity:
        """Processes the user's input string and returns a pint.Quantity object (or None).
        If the input is invalid, a warning is displayed to the user (and None is returned).
        """
        # preprocessing
        if preprocessor:
            try:
                input_string = preprocessor(input_string)
            except Exception as err:
                raise QuantityTextInputException(f"Runtime issue: Error while preprocessing input '{input_string}' with {preprocessor}: {err}")
            
        # processing
        if is_input_blank(input_string):
            return None
        quantity = parse_input_to_quantity(input_string)
        if quantity is None:
            return None
        if not is_quantity_of_mandatory_dimension(quantity):
            return None
        if not is_quantity_within_limits(quantity):
            return None

        # output
        if output_unit:
            try:
                _output_unit_ = parse_input_to_quantity(output_unit)
                quantity.ito(_output_unit_)  # convert unit in-place
            except Exception as err:
                raise QuantityTextInputUnitError(f"Error while converting to output unit '{output_unit}': {err}")
        return quantity


    # core logic    
    validate_parameters()  # problem -> QuantityTextInputException
    input_string = st.text_input(label, **kwargs)
    return process_input(input_string)  # returns a pint.Quantity object (or None)
