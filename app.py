import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Title
st.title("Smart Study Analyzer")

# Dummy data
data = pd.DataFrame({
    "hours_studied": [2,4,6,8],
    "sleep_hours": [5,6,7,8],
    "distractions": [8,6,4,2],
    "attendance": [60,70,80,90],
    "grade": [50,60,70,85]
})

X = data[['hours_studied','sleep_hours','distractions','attendance']]
y = data['grade']

model = LinearRegression()
model.fit(X,y)

# Inputs
hours = st.slider("Study Hours", 1, 10)
sleep = st.slider("Sleep Hours", 1, 10)
distractions = st.slider("Distractions", 1, 10)
attendance = st.slider("Attendance", 0, 100)

# Button
if st.button("Predict"):
    input_data = pd.DataFrame([{
        'hours_studied': hours,
        'sleep_hours': sleep,
        'distractions': distractions,
        'attendance': attendance
    }])
    
    prediction = model.predict(input_data)[0]
    
    st.write("Predicted Grade:", prediction)