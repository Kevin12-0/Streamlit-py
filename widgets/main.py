import streamlit as st

car_list = ["toyota", "fiat", "ford", "audi"]

car = st.text_input("Tipo de carro")
button = st.button("Verificar existencia")
st.write(car, button)

if button == True:
    have_it = car.lower() in car_list
    if have_it:
        st.write("Auto en el inventario")
    else:
        st.write("No se encontro en el inventario")