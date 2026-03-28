#Name: SAVALIYA UTTAM PANKAJBHAI
#Registration Number: 25BAS10005
#Course: Fundamentals of AI and ML


import pickle
import numpy as np

model = pickle.load(open("notebook.pkl", "rb"))

print("=== Health Risk Predictor (CLI) ===")

age = int(input("Age: "))
diet = input("Diet (Poor/Average/Good): ")
exercise = int(input("Exercise days/week: "))
sleep = float(input("Sleep hours: "))
stress = input("Stress (Low/Medium/High): ")
bmi = float(input("BMI: "))
smoking = input("Smoking (Yes/No): ")
alcohol = input("Alcohol (Low/Medium/High): ")
family = input("Family history (Yes/No): ")

diet_map = {'Poor': 0, 'Average': 1, 'Good': 2}
stress_map = {'Low': 0, 'Medium': 1, 'High': 2}
smoking_map = {'No': 0, 'Yes': 1}
alcohol_map = {'Low': 0, 'Medium': 1, 'High': 2}
family_map = {'No': 0, 'Yes': 1}

data = np.array([[
    age,
    diet_map[diet],
    exercise,
    sleep,
    stress_map[stress],
    bmi,
    smoking_map[smoking],
    alcohol_map[alcohol],
    family_map[family]
]])

prediction = model.predict(data)

risk_map = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}

print("\nResult:", risk_map[prediction[0]])
