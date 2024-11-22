# Importing Important Libraries
import pickle
import streamlit as st
import numpy as np

# Load model
model_diabetes = pickle.load(open('model_diabetes_logistic.sav', 'rb'))

# Page title and description
st.title("🩺 Diabetes Prediction App")
st.markdown("""
Welcome to the **Diabetes Prediction App**! 
Fill out the form below with relevant health data to predict the likelihood of diabetes.
""")

# Sidebar
st.sidebar.title("ℹ️ Instructions")
st.sidebar.markdown("""
- Provide accurate health parameters in the input fields.
- Click the **Predict Diabetes** button to see the result.
""")

# Create sections for inputs
st.header("📋 Patient Information")

# Two-column layout for inputs
col1, col2 = st.columns(2)

with col1:
    pregnancies_option = st.radio("🧪 Are You Pregnant? (Yes/No)", ("Yes", "No"))
    Pregnancies = 1 if pregnancies_option == "Yes" else 0
    BloodPressure = st.number_input("💓 Blood Pressure (mm Hg)", min_value=0, max_value=200, step=1, help="Enter your blood pressure value.")

with col2:
    Glucose = st.number_input("🩸 Glucose Level (mg/dL)", min_value=0, max_value=300, step=1, help="Enter your glucose level.")
    SkinThickness = st.number_input("📏 Skin Thickness (mm)", min_value=0, max_value=100, step=1, help="Enter the thickness of your skin.")

with col1:
    Insulin = st.number_input("🧬 Insulin Level (μU/mL)", min_value=0, max_value=900, step=1, help="Enter your insulin level.")
    DiabetesPedigreeFunction = st.number_input(
        "📈 Diabetes Pedigree Function", 
        min_value=0.0, max_value=2.5, step=0.01, 
        help="Enter the genetic diabetes pedigree function value."
    )

with col2:
    BMI = st.number_input("⚖️ BMI (Body Mass Index)", min_value=0.0, max_value=100.0, step=0.1, help="Enter your BMI value.")
    Age = st.number_input("🎂 Age (years)", min_value=0, max_value=120, step=1, help="Enter your age.")

# Prediction section
st.header("🔍 Prediction Result")
diabetes_diagnosis = ""

# Prediction button
if st.button("🚀 Predict Diabetes"):
    diabetes_prediction = model_diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if diabetes_prediction[0] == 1:
        diabetes_diagnosis = "The patient **has diabetes**."
        st.error(diabetes_diagnosis)  # Display in red
    else:
        diabetes_diagnosis = "The patient **does not have diabetes**."
        st.success(diabetes_diagnosis)  # Display in green
else:
    st.info("Click the **Predict Diabetes** button to get a result.")

# Footer
st.markdown("---")
st.markdown("💡 **Disclaimer:** This prediction is for informational purposes only and should not be considered medical advice. Please consult a healthcare professional for an accurate diagnosis.")
