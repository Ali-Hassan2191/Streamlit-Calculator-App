import streamlit as st

# Page configuration
st.set_page_config(page_title="Calculator App", page_icon="🧮", layout="centered")

# App title
st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations quickly and easily!")

# Input fields
num1 = st.number_input("Enter first number:", step=1.0, format="%.6f")
num2 = st.number_input("Enter second number:", step=1.0, format="%.6f")

# Operation selection
operation = st.selectbox(
    "Select Operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# Perform calculation
if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
            st.success(f"✅ Result: {num1} + {num2} = {result}")
        elif operation == "Subtraction (-)":
            result = num1 - num2
            st.success(f"✅ Result: {num1} - {num2} = {result}")
        elif operation == "Multiplication (×)":
            result = num1 * num2
            st.success(f"✅ Result: {num1} × {num2} = {result}")
        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("❌ Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                st.success(f"✅ Result: {num1} ÷ {num2} = {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown("""
---
**Made with ❤️ using Streamlit**
""")
