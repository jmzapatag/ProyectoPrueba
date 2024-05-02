import streamlit as st
from PIL import Image

st.title("entrada")
image = Image.open('entrada.jpg')

st.image(image)
