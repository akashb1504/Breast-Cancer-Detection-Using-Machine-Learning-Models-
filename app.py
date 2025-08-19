import streamlit as st
import pickle
import numpy as np

# Load saved model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("🩺 Breast Cancer Prediction App")
st.write("Enter the feature values below to predict whether the tumor is **Benign (B)** or **Malignant (M)**.")

# First row: 4 inputs
col1, col2, col3, col4 = st.columns(4)
radius_mean = col1.number_input("Radius Mean", min_value=0.0, step=0.01)
texture_mean = col2.number_input("Texture Mean", min_value=0.0, step=0.01)
perimeter_mean = col3.number_input("Perimeter Mean", min_value=0.0, step=0.01)
area_mean = col4.number_input("Area Mean", min_value=0.0, step=0.01)

# Second row: 4 inputs
col5, col6, col7, col8 = st.columns(4)
smoothness_mean = col5.number_input("Smoothness Mean", min_value=0.0, step=0.0001, format="%.5f")
compactness_mean = col6.number_input("Compactness Mean", min_value=0.0, step=0.0001, format="%.5f")
concavity_mean = col7.number_input("Concavity Mean", min_value=0.0, step=0.0001, format="%.5f")
concave_points_mean = col8.number_input("Concave Points Mean", min_value=0.0, step=0.0001, format="%.5f")

# Prediction button
if st.button("🔍 Predict"):
    # Collect input features
    input_data = np.array([[radius_mean, texture_mean, perimeter_mean, area_mean,
                            smoothness_mean, compactness_mean, concavity_mean, concave_points_mean]])
    
    # Check if all values are still 0 (default)
    if np.all(input_data == 0):
        st.warning("⚠️ Please enter values for all features before prediction.")
    else:
        # Scale input
        input_scaled = scaler.transform(input_data)
        
        # Predict
        prediction = model.predict(input_scaled)[0]
        
        # Output
        if prediction == 1:  # malignant
            st.error("⚠️ The prediction is **Malignant (M)**")
        else:  # benign
            st.success("✅ The prediction is **Benign (B)**")
