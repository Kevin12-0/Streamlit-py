import streamlit as st
import os

st.header("botones tipo Toggles")

# variables para los archivos
video = os.path.join(
    "video\Jackpot _ Devil May Cry _ Official Soundtrack _ Netflix.publer.com.mp4"
)
img = os.path.join("img\scribe-logo-png_seeklogo-286686.png")
audio = os.path.join("audio\Jósean Log - Doma.mp3")
# calumnas para los toggle
buttons = st.columns(3)

# asignacion de columnas
with buttons[0]:
    toggle_video = st.toggle("Avilitar Video")
with buttons[1]:
    toggle_img = st.toggle("avilitar imagen")
with buttons[2]:
    toggle_audio = st.toggle("Avilitar Audio")

# si algun toggle se avilita meutra el archivo
if toggle_video:
    st.video(video)
if toggle_img:
    st.image(image=img, width=100)
if toggle_audio:
    st.audio(audio)
