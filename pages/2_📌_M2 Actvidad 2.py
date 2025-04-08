import streamlit as st
import pandas as pd
import io
from contextlib import redirect_stdout

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

df = pd.read_csv("static/datasets/estudiantes-colombia.csv")

st.dataframe(df)

st.subheader('Primeras 5 filas del dataset')
st.write(df.head()) 

st.subheader('Últimas 5 filas del dataset')
st.write(df.tail()) 


st.subheader('Muestra un resumen usando el comando .info')

f = io.StringIO()
with redirect_stdout(f):
    df.info()
s = f.getvalue() 

st.text(s)

st.subheader('Muestra un resumen usando el comando .describe')

st.write(df.describe())

st.subheader ('Nombre, edad, y promedio')

st.write(df[['nombre', 'edad','promedio']])

st.subheader('Seleccion de promedios')

opcion = st.selectbox("Selecciona el rango que deseas explorar", 

    ["5.0 - 3.5", "3.4 - 2.5", "2.5-0.0"])

if opcion == "5.0 - 3.5":
    # Filtra los estudiantes con promedio entre 5.0 y 3.5
    resultado = df[(df['promedio'] >= 3.5) & (df['promedio'] <= 5.0)]
    st.write(resultado)

elif opcion == "3.4 - 2.5":
    # Filtra los estudiantes con promedio entre 3.4 y 2.5
    resultado = df[(df['promedio'] >= 2.5) & (df['promedio'] < 3.5)]
    st.write(resultado)
    
elif opcion == "2.5-0.0":
    # Filtra los estudiantes con promedio entre 2.5 y 0.0
    resultado = df[(df['promedio'] >= 0.0) & (df['promedio'] < 2.5)]
    st.write(resultado)