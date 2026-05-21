import streamlit as st

st.header("Radio Button")

if (
    "visibility" not in st.session_state
):  # si no hay nada seleccionado desde el principio lo mantiene activo
    st.session_state.disabled = False

radio_button = st.radio(
    "Selecciona tu curso",
    [
        "HTML & CSS :rainbow:",
        "JavaScript :camel:",
        "C# :cup_with_straw:",
    ],  # se puede pasar los radio button por medio de una lista
    index=None,  # al tener desabilitado el index, no aparece ninguno sleecionado por defecto
    # funciona por index de la lista donde [0] es el primer objeto de la lita
    disabled=st.session_state.disabled,  # se desabbilita la seeccion de los radio button al tenerlo en True
    key="visibility",
)


if radio_button == "HTML & CSS :rainbow:":
    st.write("Seleccionaste HTML & CSS")
    st.session_state.disabled = True  # una vez con una seleccion lo desactiva
if radio_button == "JavaScript :camel:":
    st.write("Seleccionaste JavaScript :camel:")
    st.session_state.disabled = True  # una vez con una seleccion lo desactiva
if radio_button == "C# :cup_with_straw:":
    st.write("Seleccionaste C# :cup_with_straw:")
    st.session_state.disabled = True  # una vez con una seleccion lo desactiva
