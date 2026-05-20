import streamlit as st

st.image("img\pumas-logo-70-anos-aniversario.jpg")
name = st.text_input("Introduce el nombre de la imagen")
st.write(name)

with open("img\pumas-logo-70-anos-aniversario.jpg", "rb") as file:
    btn = st.download_button(
        label="Descargar Imagen",  # texto del botton #
        data=file,
        file_name=name,
        mime="image/png",
    )
