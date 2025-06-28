import streamlit as st
import numpy as np
import joblib
import json

# Load model
model = joblib.load(r'model/BHP.joblib')

# Load data columns
with open(r'model\columns.json', 'r') as f:
    data_columns = json.load(f)["data_columns"]

location_list = data_columns[3:]  # exclude sqft, bath, bhk

st.title("🏠 Bangalore Home Price Prediction")

# Inputs
location = st.selectbox("Select Location", sorted(location_list))
sqft = st.number_input("Total Square Feet", min_value=100, max_value=10000, step=50)
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)
bhk = st.number_input("Number of Bedrooms (BHK)", min_value=1, max_value=10, step=1)

# Prediction Function
def predict_price(location, sqft, bath, bhk):
    X = np.zeros(len(data_columns))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk

    if location in data_columns:
        loc_index = data_columns.index(location)
        X[loc_index] = 1

    return model.predict([X])[0]

if st.button("Predict Price"):
    predicted_price = predict_price(location, sqft, bath, bhk)
    st.success(f"Estimated Price: ₹ {predicted_price:.2f} Lakhs")
