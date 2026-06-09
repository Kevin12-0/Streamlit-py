import streamlit as st
import os

size = st.slider(
    "Tamaño de la imagen",
    100,  # rango menor
    400,  # rango mayor
    150,  # valor por defecto
)

imag = os.path.join("img/devil.jpg")
st.image(imag, width=size)  # se pasa la variable size, para que cambie el tamaño
