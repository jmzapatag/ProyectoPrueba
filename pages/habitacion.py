import streamlit as st
from PIL import Image

st.title("habitacion")
image = Image.open('habitacion.jpg')

st.image(image)
