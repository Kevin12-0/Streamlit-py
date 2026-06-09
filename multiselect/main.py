import streamlit as st
import os

options = st.multiselect(
    "¿Selecciona tus juegos favoritos?",  # Pregunta
    ["Halo", "Devil May Cry", "Resident Evil", "Mortal Kombat"],  # Opciones
    ["Halo"],  # Valor por defecto
)

for x in options:
    if x == "Halo":
        img = os.path.join("img/halo.avif")
        st.image(img, width=150, caption="Halo")
    if x == "Devil May Cry":
        img = os.path.join("img/devil.jpg")
        st.image(img, width=150, caption="Devil May Cry")
    if x == "Resident Evil":
        img = os.path.join("img/resident.avif")
        st.image(img, width=150, caption="Resident Evil")
    if x == "Mortal Kombat":
        img = os.path.join("img/1cc63f4f4b2c9a9852fabefba4ca7eea936b1ef7867811a5.avif")
        st.image(img, width=150, caption="Mortal Kombat")
