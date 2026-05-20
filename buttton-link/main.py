import streamlit as st
import os

# se puede pasar la ruta como variables con OS para una apertura mas rapida
logo_Pape = os.path.join(
    "img\plantilla-logotipo-tienda-papeleria-diseno-plano_23-2149758692.avif"
)

logo_scribe = os.path.join("img\scribe-logo-png_seeklogo-286686.png")

# Descripciones en las imagenes

caption_list = ["Logo Papepeleria", "Logo Scribe"]

# Header de la pagina
st.header("Pruebas")
# Lista de Imagenes
lista_imagenes = [logo_Pape, logo_scribe]
# imagenes
st.image(image=lista_imagenes, width=100, caption=caption_list)

st.subheader("Est prueba es para la creacion de un POS, Punto de Venta para un negocio")
st.link_button("Ir a una pagina", "https://www.youtube.com/")
