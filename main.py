import streamlit as st
import numpy as np
from scipy.optimize import minimize

# Function to minimize (quadratic function)
def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

# Streamlit app
def main():
    st.title("Quadratic Function Minimizer")
    
    st.write("This app finds the minimum of a quadratic function of the form `ax^2 + bx + c`.")
    
    # User inputs for the coefficients
    a = st.number_input("Enter the coefficient a:", value=1.0, format="%.2f")
    b = st.number_input("Enter the coefficient b:", value=0.0, format="%.2f")
    c = st.number_input("Enter the coefficient c:", value=0.0, format="%.2f")
    
    # Initial guess for the optimizer
    x0 = st.number_input("Enter the initial guess for x:", value=0.0, format="%.2f")
    
    # Define the function to be minimized
    def func_to_minimize(x):
        return quadratic_function(x, a, b, c)
    
    # Perform the minimization using SciPy
    result = minimize(func_to_minimize, x0)
    
    st.write(f"The minimum value of the function is {result.fun:.2f} at x = {result.x[0]:.2f}")
    
    # Plot the function and the minimum point
    x_values = np.linspace(-10, 10, 400)
    y_values = quadratic_function(x_values, a, b, c)
    
    st.line_chart({"y": y_values, "x": x_values})
    
if __name__ == "__main__":
    main()
