import streamlit as st
from PIL import Image

st.title("Pagina Inicial")
image = Image.open('home.jpg')

st.image(image)
