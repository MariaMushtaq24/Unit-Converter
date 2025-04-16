import streamlit as st

import pint
# foundation of unit registry
ureg = pint.UnitRegistry()

# Unit Categories
unit_categories = {
    "Time" : ["second", "minute", "hour", "day"],
    "Weight" : ["gram", "kilogram", "pound", "ounce", "ton"],
    "Length" : ["meter", "kilometer", "mile", "yard", "foot", "inch", "centimeter", "millimeter"],
    "Speed" : ["meter/second", "kilometer/hour", "mile/hour", "foot/second"],
    "Area" : ["square meter", "square kilometer", "square mile", "square yard", "square foot", "square inch", "square centimeter", "square millimeter"]
}

def convert_units(value, from_unit, to_unit):
        result = (value * ureg(from_unit)).to(to_unit)
        return round(result.magnitude, 4)

# UI on Streamlit
st.title("The Unit Converter 🔄")
st.markdown("### Convert Length, Weight, and Time Instantly!")
st.write("Select a category, enter a value, and get the conversion result in real-time.")
category = st.selectbox("Select a Category", list(unit_categories.keys()))
from_unit = st.selectbox("Select a Unit to Convert From", unit_categories[category])
to_unit = st.selectbox("Select a Unit to Convert To", unit_categories[category])
value = st.number_input(f"Enter a value in {from_unit}")
result = convert_units(value, from_unit, to_unit)
st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")