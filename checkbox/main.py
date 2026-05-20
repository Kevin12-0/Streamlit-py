import os
import streamlit as st

st.header("Pruebas de checkbox funcionales")
logo_pape = os.path.join(
    "img\plantilla-logotipo-tienda-papeleria-diseno-plano_23-2149758692.avif"
)
logo_scribe = os.path.join(
    "D:\Streamlit-py\checkbox\img\scribe-logo-png_seeklogo-286686.png"
)
list_logos = [logo_pape, logo_scribe]
caption_list = ["Logo Pape", "Lgo Scribe"]

# columnas con streamlit

checks = st.columns(2)
with checks[0]:
    images = st.checkbox("Deseas ver las fotos ?")
with checks[1]:
    codes = st.checkbox("Deseas ver el codigo?")

# si se selecciona el check box
if images:
    st.image(image=list_logos, width=100, caption=caption_list)  # muestra las imagenes
if codes:  # si se selecciona el checkbox
    st.code("SELECT * FROM DATABASE")  # se muestra el codgio
