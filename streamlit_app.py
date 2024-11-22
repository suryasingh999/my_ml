# Importing Important Libraries
import pickle
import streamlit as st
import numpy as np

# Load model
model_diabetes = pickle.load(open('model_diabetes_logistic.sav', 'rb'))

# Application title
st.title('🩺 Diabetes Prediction App')
st.markdown("This application predicts whether a patient has diabetes based on medical parameters. Please fill in the details below.")

# Organize UI into sections
st.header("Patient Information")

# User Inputs
col1, col2 = st.columns(2)

with col1:
    pregnancies_option = st.radio("Are You Pregnant? (Yes/No)", ("Yes", "No"))
    Pregnancies = 1 if pregnancies_option == "Yes" else 0

with col2:
    Glucose = st.number_input('Glucose Level', min_value=0, max_value=300, step=1, help="Enter the glucose level (mg/dL).")

with col1:
    BloodPressure = st.number_input('Blood Pressure', min_value=0, max_value=200, step=1, help="Enter the blood pressure (mm Hg).")

with col2:
    SkinThickness = st.number_input('Skin Thickness', min_value=0, max_value=100, step=1, help="Enter the skin thickness (mm).")

with col1:
    Insulin = st.number_input('Insulin Level', min_value=0, max_value=900, step=1, help="Enter the insulin level (μU/mL).")

with col2:
    BMI = st.number_input('BMI', min_value=0.0, max_value=100.0, step=0.1, help="Enter the BMI (Body Mass Index).")

with col1:
    DiabetesPedigreeFunction = st.number_input(
        'Diabetes Pedigree Function', 
        min_value=0.0, 
        max_value=2.5, 
        step=0.01, 
        help="Enter the Diabetes Pedigree Function value."
    )

with col2:
    Age = st.number_input('Age', min_value=0, max_value=120, step=1, help="Enter the age (years).")

# Prediction button and result
st.header("Prediction Result")
diabetes_diagnosis = ''

if st.button('🧪 Predict Diabetes'):
    diabetes_prediction = model_diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if diabetes_prediction[0] == 1:
        diabetes_diagnosis = 'The patient **has diabetes**.'
    else:
        diabetes_diagnosis = 'The patient **does not have diabetes**.'
    
    st.success(diabetes_diagnosis)
