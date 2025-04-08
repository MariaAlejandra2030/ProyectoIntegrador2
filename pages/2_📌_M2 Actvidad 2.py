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
Instrucciones: Usando el dataset estudiantes_colombia.csv, crea una aplicación en Streamlit que permita al usuario:

Ver las primeras 5 filas y las últimas 5 filas del dataset.
Mostrar un resumen con .info() y .describe().
Seleccionar columnas específicas (ej. "nombre", "edad", "promedio") para mostrarlas.
Filtrar estudiantes con promedio mayor a un valor definido por el usuario (usando un slider).
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

df = pd.read_csv("static/datasets/estudiantes_colombia.csv")

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