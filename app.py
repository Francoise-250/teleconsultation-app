

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# Page config with icon
# -----------------------------
st.set_page_config(
    page_title="Teleconsultation & Referral System",
    page_icon="🩺",   # You can use emojis or replace with custom icon path
    layout="centered"
)

# -----------------------------
# Dummy model training (replace with your real trained model)
# -----------------------------
np.random.seed(42)
X_dummy = np.random.randint(0, 100, (200, 8))  
y_dummy = np.random.randint(0, 2, 200)  

model = RandomForestClassifier()
model.fit(X_dummy, y_dummy)

# -----------------------------
# Streamlit app
# -----------------------------
st.title("🩺 Machine Learning Based Teleconsultation & Referral System")
st.write("Use patient information to predict whether *Referral is Required* or not.")

# Add optional logo (if you have one, e.g., 'logo.png')
# st.image("logo.png", width=120)  # uncomment if you have a logo file

# Input fields with icons
age = st.number_input("👶 Age", min_value=0, max_value=120, value=30)
sex = st.selectbox("⚧ Sex", ("Male", "Female"))
location = st.selectbox("📍 Location", ("Urban", "Rural"))
systolic_bp = st.number_input("💓 Systolic BP (mmHg)", min_value=50, max_value=200, value=120)
diastolic_bp = st.number_input("💓 Diastolic BP (mmHg)", min_value=30, max_value=120, value=80)
heart_rate = st.number_input("❤️ Heart Rate (bpm)", min_value=30, max_value=200, value=75)
body_temp = st.number_input("🌡️ Body Temperature (°C)", min_value=30.0, max_value=45.0, value=36.5)
spo2 = st.number_input("🫁 SpO2 (%)", min_value=50, max_value=100, value=98)

# Encode categorical variables
sex_val = 1 if sex == "Male" else 0
location_val = 1 if location == "Urban" else 0

# Create feature vector
features = np.array([[age, sex_val, location_val, systolic_bp, diastolic_bp, heart_rate, body_temp, spo2]])

# Predict
if st.button("🔍 Predict Referral"):
    prediction = model.predict(features)
    result = "✅ Referral Required" if prediction[0] == 1 else "❌ No Referral Needed"
    st.subheader(f"Prediction Result: {result}")