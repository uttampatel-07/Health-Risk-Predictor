#Name: SAVALIYA UTTAM PANKAJBHAI
#Registration Number: 25BAS10005
#Course: Fundamentals of AI and ML

import streamlit as st
import pickle
import numpy as np
import plotly.express as px

model = pickle.load(open("notebook.pkl","rb"))

encoders=pickle.load(open("label_encoders.pkl","rb"))

st.title("Health Risk Predictor")

age = st.slider("Age",18,80,22)
diet = st.selectbox("Diet Quality",['Poor','Average','Good'])
exercise = st.slider("Exercise Day Per Week",0,7,3)
sleep = st.slider("Sleep Hours",2,12,6)
stress = st.selectbox("Stress Level",['Low','Medium','High'])
bmi = st.number_input("BMI",10.0,40.0,22.0)
smoking = st.selectbox("Smoking",["Yes","No"])
alcohol = st.selectbox("Alcohol Consumption",["Low","Medium","Hign"])
family_history = st.selectbox("Family History Of Disease",["Yes","No"])

if st.button("Predict Risk"):

    
    diet_map = {'Poor': 0, 'Average': 1, 'Good': 2}
    stress_map = {'Low': 0, 'Medium': 1, 'High': 2}
    smoking_map = {'No': 0, 'Yes': 1}
    alcohol_map = {'Low': 0, 'Medium': 1, 'High': 2}
    family_map = {'No': 0, 'Yes': 1}

    diet_val = diet_map[diet]
    stress_val = stress_map[stress]
    smoking_val = smoking_map[smoking]
    alcohol_val = alcohol_map[alcohol]
    family_val = family_map[family_history]

    
    input_data = [
        age,
        diet_val,
        exercise,
        sleep,
        stress_val,
        bmi,
        smoking_val,
        alcohol_val,
        family_val
    ]

    
    prediction = model.predict([input_data])

    
    risk_map = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}

    st.success(risk_map[prediction[0]])
