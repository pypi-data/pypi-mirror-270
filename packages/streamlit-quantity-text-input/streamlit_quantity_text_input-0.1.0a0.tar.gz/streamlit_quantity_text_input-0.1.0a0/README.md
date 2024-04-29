# streamlit_quantity_text_input

This Python module gives you a Streamlit text input field (like `st.text_input`) for entering and processing concentrations, volumes, amounts ect. in free-text, yet in an input-safe manner.

The *quantity_text_input* field uses the **pint** library to parse the user's input as a quantity (volume, speed, concentration etc.).

### Features
* The input field can be configured to **accept only inputs of a given dimensionality** (e.g. volume) and will accept inputs in a wide range of relevant units.
* The input field can be configured to **return the input value in your preferred unit** (such as milliliters, barrels, in³ etc.). 
* In case of user input error, the input field displays a **helpful error message to the user** immediately below the field.
* Developers can specify a callable for **pre-processing the user's input** before it is handed over to the input field's parsing algorithm.
* The return value, a pint.Quantity instance, can be used downstream for **unit-aware calculations**.


## Getting started

$ `pip install streamlit-quantity-text-input`

    from streamlit_quantity_text_input import quantity_text_input
  
    vol = quantity_text_input(
        "Please input a volume:",
        mandatory_dimension="volume",
        output_unit="ml",
        lower_limit="0 l")
    
    print(f"You input volume is: {vol if vol else 'pending'}")

Check out the accompanying `demo.py` for a more detailed example and documentation.


## Roadmap

Wanted but not yet planned:

* **Test cases:** Unit tests, perhaps via the doctest module.

* **Flag:** `relaxed_time_input`. Implement a flag to allow a much broader range of types of time inputs to be parsed correctly, consistently (e.g. `1h45`, `1hrs3minutes`, `2wks60'45"` etc.). Bonus points for offering a solution that also addresses Danish spellings (perhaps as a pre-parser).

* **Fool-profing the math parser:** The pint library treats scalars and units equally, which can lead to some unexpected parsing when mixing scalars and units (`1 m / 2 s` parses into `1*m/2*s`=`½ m*s`, not `½ m/s`). Presumably, this can be fixed by tokenizing the input string and 'gluing' scalars and their abutting unit(s) together with parenthesis (`((1*m)/(2*s))`). However, writing the tokenizer could be non-trivial.

## License

See LICENSE.txt

## Project status

New as of April 2024.
