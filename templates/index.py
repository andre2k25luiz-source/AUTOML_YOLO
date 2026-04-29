import streamlit as st
import requests

st.title("AutoML YOLO - One Shot")

uploaded = st.file_uploader("Envie uma imagem do objeto")

if uploaded:
    if st.button("Treinar modelo"):
        files = {"image": uploaded.getvalue()}
        res = requests.post("http://localhost:5000/train", files=files)
        st.write(res.json())

    if st.button("Testar imagem"):
        files = {"image": uploaded.getvalue()}
        res = requests.post("http://localhost:5000/predict", files=files)
        st.write(res.json())