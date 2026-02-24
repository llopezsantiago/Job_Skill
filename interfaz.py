#importamos la librerias correspondintes
import streamlit as st
import plotly.express as px
from Carga_datos import cargar_limpiar_datos as cld #Para usar la funcion cargar_limpiar_data del archivo Cargar_datos hacemos lo siguiente:
from pes_geografia import geografia as geo
from pes_salarial import salario as sal
from pes_remoto import remoto as rem
from pes_habilidades import habilidades as hab

#configuramos la pagina web
st.set_page_config(
    page_title="Mercado Laboral 2024", 
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
    )

def cambiar_fondo_color(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Ejemplo de uso (puedes usar nombres de colores o Hexadecimal)
cambiar_fondo_color("#FFFFFF")

#Función Unificada de Estilo (Fondo + Letras)
def aplicar_estilos_globales(fondo, texto_principal, texto_titulos):
    st.markdown(
        f"""
        <style>
        /* Fondo de la aplicación */
        .stApp {{
            background-color: {fondo};
        }}

        /* Color de texto general (párrafos, listas, etc.) */
        .stApp p, .stApp span, .stApp label, .stApp li {{
            color: {texto_principal} !important;
        }}

        /* Color de los Títulos (h1, h2, h3) */
        h1, h2, h3, h4, h5, h6 {{
            color: {texto_titulos} !important;
        }}

        /* Color de los nombres de las Pestañas (Tabs) */
        button[data-baseweb="tab"] div p {{
            color: {texto_titulos} !important;
            font-weight: bold;
        }}
        
        /* Color de los textos en la barra lateral */
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {{
            color: {texto_principal} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

#Aplicamos los colores (Fondo Blanco, Texto Azul Marino, Títulos Azul Oscuro)
aplicar_estilos_globales("#FFFFFF", "#1E3A8A", "#0F172A")

#Llamamos la funcion cargar_limpiar_datos as cld del archivo Cargar_datos
data = cld()

#colocamos el titulo visual de la pagina
st.title("Mercado laboral")

#creamos las pestañas con nombres referentes a nustros obejtivos especificos
pestaña_resumen, pestaña_salarial, pestaña_remoto, pestaña_geogafria, pestaña_skills, pestaña_empresa = st.tabs([
    "Resumen estadistico",
    "Distribución Salarial", 
    "Impacto Remoto", 
    "Análisis Geográfico", 
    "Habilidades Críticas", 
    "Tamaño de Empresa"
    ])

#1. Pestaña resumen
with pestaña_resumen:
    st.header("Analisis de Rentabilidad por Industria")
    

#2. Pestaña salarial
with pestaña_salarial:
    st.header("Estadistica descriptiva del salario en las industrias")
    sal()

#3. Pestaña de trabajo remoto
with pestaña_remoto:
    st.header("Análisis del impacto salarial en los trabajos remotos")
    rem()
    

#4. Pestaña de geografia
with pestaña_geogafria:
    st.header("Análisis geografico del mercado laboral")
    geo()

#1. Pestaña de habilidades
with pestaña_skills:
    st.header("Habilidades más Demandadas por Sector")
    hab()

#1. Pestaña tamaño de la empresa
with pestaña_empresa:
    st.header("Análisis de Rentabilidad por Industria")
    