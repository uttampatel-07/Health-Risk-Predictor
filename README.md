# Health Risk Predictor

## Student Details

**Name:** SAVALIYA UTTAM PANKAJBHAI

**Registration Number:** 25BAS10005

**Course:** Fundamentals of AI and ML

---

##   Project Description

The **Health Risk Predictor** is an AI/ML-based application that predicts an individual's health risk level (Low, Medium, High) based on lifestyle and health-related inputs.

The system uses a trained machine learning model to analyze multiple factors such as age, diet quality, exercise frequency, sleep duration, stress level, BMI, smoking habits, alcohol consumption, and family medical history.

This project provides both:

* A **Command Line Interface (CLI)** (mandatory requirement)
* A **Streamlit-based User Interface (UI)** (for better interaction)

---

##  Problem Statement

Many individuals are unaware of how their daily lifestyle habits affect their health. This project helps in predicting health risk early and encourages users to adopt healthier habits.

---

##  Methodology

* Dataset Source: Kaggle
* Data Preprocessing: Encoding categorical variables using mapping techniques
* Model Training: Performed using machine learning algorithms in Jupyter Notebook
* Model Saving: Stored using Pickle (`notebook.pkl`)
* Prediction: Performed using trained model in both CLI and UI

---

##  Dataset Information

The dataset used in this project is obtained from Kaggle and includes the following features:

* Age
* Diet Quality
* Exercise Frequency
* Sleep Duration
* Stress Level
* BMI
* Smoking Habits
* Alcohol Consumption
* Family History of Disease

---

##  Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Streamlit
* Plotly

---

##  Project Structure

```
health-risk-predictor/
│── app.py
│── main.py
│── notebook.ipynb
│── notebook.pkl
│── label_encoders.pkl
│── synthetic_health_data.csv
│── README.md
│── report.pdf
│── requirements.txt
```

---



##  How to Run the Project

###   Run CLI Version (MANDATORY)

```
python main.py
```

 This version takes user input from terminal and predicts health risk.
(Implemented in )

---

###  Run UI Version (OPTIONAL)

```
streamlit run app.py
```

 This opens an interactive web interface for prediction.
(Implemented in )

---

##  Features

* Predicts health risk (Low / Medium / High)
* Uses trained machine learning model
* CLI-based execution (as required by course)
* Interactive UI using Streamlit
* Handles multiple health parameters
* Simple and user-friendly design

---

##  Sample CLI Output

```
=== Health Risk Predictor (CLI) ===

Age: 25
Diet: Good
Exercise days/week: 4
Sleep hours: 7
Stress: Low
BMI: 22
Smoking: No
Alcohol: Low
Family history: No

Result: Low Risk
```

---

##  Notes

* The dataset is sourced from Kaggle and used for educational purposes.
* Predictions are based on machine learning model and are not medically certified.
* CLI version is mandatory for evaluation as per project guidelines.

---

##  Future Improvements

* Use real-world healthcare datasets
* Improve model accuracy
* Add more health parameters
* Deploy as a full web application

---

##  Conclusion

This project demonstrates how machine learning can be used to predict health risks based on lifestyle factors. It highlights the importance of AI in assisting individuals to make better health decisions.

---
