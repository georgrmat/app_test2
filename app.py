import streamlit as st

# Streamlit app title
st.title("Simple Number Sum Calculator")

# User input: Ask for two numbers
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

# Calculate the sum
sum_result = num1 + num2

# Display the result
st.write(f"The sum of {num1} and {num2} is: {sum_result}")
