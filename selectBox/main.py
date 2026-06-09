import streamlit as st
import os

game_info = [
    {"Game": "Resident Evil", "Make": "Capcom"},
    {"Game": "Devil May Cry", "Make": "Capcom"},
    {"Game": "Mortal Kombat", "Make": "Warner"},
    {"Game": "Halo", "Make": "343"},
]

st.header("Selecciona tu juego")

option = st.selectbox(
    "¿Que juegos vas a escoger?",  # Opcion o pregunta para saber que se seleccdiona
    [
        game_info[0]["Game"] + " " + game_info[0]["Make"],
        game_info[1]["Game"] + " " + game_info[1]["Make"],
        game_info[2]["Game"] + " " + game_info[2]["Make"],
        game_info[3]["Game"] + " " + game_info[3]["Make"],
    ],
)

if option == game_info[0]["Game"] + " " + game_info[0]["Make"]:
    img = os.path.join("img/resident.avif")
    st.image(img, width=300)
if option == game_info[1]["Game"] + " " + game_info[1]["Make"]:
    img = os.path.join("img/devil.jpg")
    st.image(img, width=300)
if option == game_info[2]["Game"] + " " + game_info[2]["Make"]:
    img = os.path.join("img/1cc63f4f4b2c9a9852fabefba4ca7eea936b1ef7867811a5.avif")
    st.image(img, width=300)
if option == game_info[3]["Game"] + " " + game_info[3]["Make"]:
    img = os.path.join("img/halo.avif")
    st.image(img, width=300)
