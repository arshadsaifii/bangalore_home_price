# bangalore_home_price
This project predicts house prices in Bangalore using a Machine Learning model. The app is built using Streamlit and trained on real housing data. Users can input parameters like location, square feet, number of bathrooms, and BHK to estimate the property price.

🧠 Features
Cleaned and preprocessed real-world housing data
Outlier removal for square footage and price per sq. ft.
One-hot encoding of Bangalore locations
Linear Regression model with best score ~87%
Interactive Streamlit UI
Live price prediction

🛠️ How to Run Locally
1. Clone the repository

2. pip install -r requirements.txt

3. streamlit run app.py

📦 Model Input Example
{
  "location": "Whitefield",
  "total_sqft": 1000,
  "bath": 2,
  "bhk": 2
}

📊 Model Performance
Model Used: Linear Regression

Cross-Validation Accuracy: ~82%

Test Set R² Score: ~87%
