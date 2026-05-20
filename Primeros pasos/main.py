import streamlit as st
import pandas as pd

st.title("Hola, Yo soy Kevin")  # titulo
st.header("esto es un header")  # header
st.subheader("Esto es un subheader")  # sub header
st.text("Esto es un Texto")  # texto plano

# Mas elementos para crear una pagina web
# Se puede usar directamente el lenguaje Markdown
# Es el mismo lenguaje que se ultilisa para hacer los README.md

st.markdown("# Turtle Code")
st.markdown("## Turtle Code")
st.markdown("### Turtle Code")
st.markdown("**Turtle** Code")
st.markdown("*Turtle* Code")

# Para fragmentos de codigo

st.markdown("> Turtle* Code")

st.markdown("1. Fisrt Item\n2. Second Item")

# pasar variables a markdown

str = "print('Helo world')"
# Bloque de codigo
st.code(str)

# Divisor

st.markdown("---")

# Link para Rederigir a otro sitio

st.markdown("[Google](https://www.google.com)")

# Tbala

text = """
|syntax|description|
|---------|---------|
|header|title|
"""
st.markdown(text)

# Uso de formato Json

st.text("Json")
json = {"a": 1, "b": 2, "c": 3}
st.json(json)

## funcionnes metric

st.metric(
    label="Win Speed",  # titulo
    value="70ms",  # Valor a mostrar en la p'agina web
    delta="-2.9",
)  # si el valor es positivo se muestra en tonalidad verde, si es negativo en tonalidad roja

#Crear una tabla desde un diccionario
table = {"Column 1": [1, 2, 3, 4, 5], "Column 2": [6, 7, 8, 9, 10]}
st.table(table) # Se pasa la tabal como varibale 


# Convertir tu diccionario a dataframe
# Converit tu diccionario te permitira
# descargar
# buscar
# ampliar la tabla

st.dataframe(table)


