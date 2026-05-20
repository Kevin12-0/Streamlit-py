import streamlit as st

# Agregar una imagen
st.image(
    "img/pumas-logo-70-anos-aniversario.jpg", caption="Esto es una imagen", width=400
)

# Agregar audio
st.audio(
    "audio/Jósean Log - Doma.mp3", start_time=100
)  # start_time --> para saber en que segundo quieres que que por defecto al iniciaar la pagina

# Inserter un video

st.video(
    "video\Jackpot _ Devil May Cry _ Official Soundtrack _ Netflix.publer.com.mp4",
    start_time=43,
)
