import requests
import streamlit as st

API_URL = "http://localhost:8000/predict"

st.set_page_config(page_title="Iris Classifier", page_icon="🌸")

st.markdown(
    """
    <style>
    .block-container { max-width: 720px; padding-top: 2rem; }
    h1 { text-align: center; color: #C2185B; }
    .subtitle { text-align: center; color: #8E4162; margin-bottom: 1.5rem; }
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #F48FB1, #E75480);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1rem;
        font-weight: 600;
    }
    div.stButton > button:hover { background: #D81B60; color: white; }
    .result-card {
        background: #FFFFFF;
        border: 2px solid #F8BBD0;
        border-radius: 16px;
        padding: 1.2rem;
        text-align: center;
        margin-top: 1rem;
        box-shadow: 0 4px 12px rgba(231, 84, 128, 0.15);
    }
    .result-card .emoji { font-size: 3rem; }
    .result-card .name { font-size: 1.8rem; font-weight: 700; color: #C2185B; }
    </style>
    """,
    unsafe_allow_html=True,
)

EMOJI = {"setosa": "🌸", "versicolor": "🌺", "virginica": "🌷"}

st.title("🌸 Iris Classifier")
st.markdown(
    '<div class="subtitle">Введите размеры цветка, и модель определит его вид</div>',
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)
sepal_length = c1.number_input("Sepal length (см)", 0.0, 10.0, 5.1, 0.1)
sepal_width = c2.number_input("Sepal width (см)", 0.0, 10.0, 3.5, 0.1)

c3, c4 = st.columns(2)
petal_length = c3.number_input("Petal length (см)", 0.0, 10.0, 1.4, 0.1)
petal_width = c4.number_input("Petal width (см)", 0.0, 10.0, 0.2, 0.1)

if st.button("Определить вид 🌷"):
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
        name = result["class_name"]
        st.markdown(
            f"""
            <div class="result-card">
                <div class="emoji">{EMOJI.get(name, "🌸")}</div>
                <div class="name">{name}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with st.expander("Ответ API"):
            st.json(result)
    except requests.exceptions.RequestException as e:
        st.error(f"Не удалось связаться с API: {e}")