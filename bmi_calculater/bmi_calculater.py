import streamlit as st

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight "
    elif 18.5 <= bmi < 25:
        return "Normal "
    elif 25 <= bmi < 30:
        return "Overweight "
    else:
        return "Obese "

st.title("🧮 BMI Calculator")

weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.5)
height = st.number_input("Enter your height (cm)", min_value=30.0, step=0.5)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    st.success(f"Your BMI is: {bmi}")
    st.info(f"Category: {category}")
