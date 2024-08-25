import streamlit as st
import requests

st.title("Basic Calculator")

operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

x = st.slider("Select value for x", 0, 100)
y = st.slider("Select value for y", 0, 100)

if st.button("Calculate"):
    url = f"http://backend:8080/{operation.lower()}"
    response = requests.post(url, json={"x": x, "y": y})
    result = response.json().get("result", "Error")
    st.write(f"Result: {result}")