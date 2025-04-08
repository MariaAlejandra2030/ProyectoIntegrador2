import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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

# ---------------------- Diccionario ----------------------
st.header("📚 DataFrame desde un Diccionario")

libros = {
    "título": ["Cien Años de Soledad", "Rayuela", "Pedro Páramo", "Ficciones"],
    "autor": ["Gabriel García Márquez", "Julio Cortázar", "Juan Rulfo", "Jorge Luis Borges"],
    "año de publicación": [1967, 1963, 1955, 1944],
    "género": ["Realismo Mágico", "Narrativa", "Realismo Mágico", "Ficción"]
}

df_libros = pd.DataFrame(libros)
st.dataframe(df_libros)

# ---------------------- Lista de diccionarios ----------------------
st.header("🌆 Información de Ciudades")

ciudades = [
    {"nombre": "Bogotá", "población": 8000000, "país": "Colombia"},
    {"nombre": "Buenos Aires", "población": 3000000, "país": "Argentina"},
    {"nombre": "Lima", "población": 9000000, "país": "Perú"},
    {"nombre": "Quito", "población": 2000000, "país": "Ecuador"}
]

df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)

# ---------------------- Lista de listas ----------------------
st.header("📦 Productos en Inventario")

productos = [
    ["Laptop", 2500, 15],
    ["Mouse", 25, 200],
    ["Teclado", 45, 120]
]

df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_productos)

# ---------------------- Series ----------------------
st.header("👥 Datos de Personas")

nombres = pd.Series(["Ana", "Luis", "Carlos", "María"])
edades = pd.Series([23, 34, 29, 41])
ciudades = pd.Series(["Bogotá", "Medellín", "Cali", "Barranquilla"])

df_personas = pd.DataFrame({
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
})
st.dataframe(df_personas)

# ---------------------- CSV ----------------------
st.header("📄 Datos desde CSV")

try:
    df_csv = pd.read_csv("static/data.csv")
    st.dataframe(df_csv)
except FileNotFoundError:
    st.error("Archivo CSV no encontrado. Asegúrate de que 'data.csv' esté en la carpeta 'static'.")

# ---------------------- Excel ----------------------
st.header("📊 Datos desde Excel")

try:
    df_excel = pd.read_excel("static/data.xlsx")
    st.dataframe(df_excel)
except FileNotFoundError:
    st.error("Archivo Excel no encontrado. Asegúrate de que 'data.xlsx' esté en la carpeta 'static'.")
except Exception as e:
    st.error(f"Error al leer Excel: {e}")

# ---------------------- JSON ----------------------
st.header("🧾 Datos de Usuarios desde JSON")

try:
    df_json = pd.read_json("static/data.json")
    st.dataframe(df_json)
except FileNotFoundError:
    st.error("Archivo JSON no encontrado. Asegúrate de que 'data.json' esté en la carpeta 'static'.")

# ---------------------- URL ----------------------
st.header("🌐 Datos desde URL")

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
try:
    df_url = pd.read_csv(url)
    st.dataframe(df_url)
except:
    st.error("No se pudo cargar el archivo desde la URL.")

# ---------------------- SQLite ----------------------
st.header("💾 Datos desde SQLite")

try:
    conn = sqlite3.connect("static/estudiantes.db")
    conn.execute("CREATE TABLE IF NOT EXISTS notas (nombre TEXT, calificacion REAL)")
    conn.execute("INSERT INTO notas (nombre, calificacion) VALUES ('Juan', 4.5), ('Ana', 3.8), ('Luis', 4.0)")
    conn.commit()
    df_sql = pd.read_sql("SELECT * FROM notas", conn)
    conn.close()
    st.dataframe(df_sql)
except Exception as e:
    st.error(f"Error al consultar SQLite: {e}")

# ---------------------- NumPy ----------------------
st.header("📐 Datos desde NumPy")

array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

df_numpy = pd.DataFrame(array, columns=["A", "B", "C"])
st.dataframe(df_numpy)

