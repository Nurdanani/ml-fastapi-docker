import requests
import streamlit as st

API_URL = "http://localhost:8000/predict"

st.set_page_config(page_title="Iris Classifier", page_icon="🌸")
st.title("🌸 Iris Classifier")
st.write("Введите размеры цветка, и модель определит его вид.")

col1, col2 = st.columns(2)
with col1:
    sepal_length = st.number_input("Sepal length (см)", 0.0, 10.0, 5.1, 0.1)
    sepal_width = st.number_input("Sepal width (см)", 0.0, 10.0, 3.5, 0.1)
with col2:
    petal_length = st.number_input("Petal length (см)", 0.0, 10.0, 1.4, 0.1)
    petal_width = st.number_input("Petal width (см)", 0.0, 10.0, 0.2, 0.1)

if st.button("Predict"):
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }
    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()
        st.success(f"Вид цветка: **{result['class_name']}**")
        st.json(result)
    except requests.exceptions.RequestException as e:
        st.error(f"Не удалось связаться с API: {e}")