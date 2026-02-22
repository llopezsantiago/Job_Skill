#importamos la librerias correspondintes
import streamlit as st
import plotly.express as px
from Carga_datos import cargar_limpiar_datos as cld #Para usar la funcion cargar_limpiar_data del archivo Cargar_datos hacemos lo siguiente:
from pes_geografia import geografia as geo
from pes_salarial import salario as sal

#configuramos la pagina web
st.set_page_config(page_title="Analisis del mercado laboral", layout="wide")

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
    st.header("Análisis de Rentabilidad por Industria")
    

#2. Pestaña resumen
with pestaña_salarial:
    st.header("Analisis descriptivo del salario por industria")
    sal()

#3. Pestaña resumen
with pestaña_remoto:
    st.header("Análisis de Rentabilidad por Industria")
    

#4. Pestaña resumen
with pestaña_geogafria:
    st.header("Análisis de Rentabilidad por Industria")
    geo()

#1. Pestaña resumen
with pestaña_skills:
    st.header("Análisis de Rentabilidad por Industria")
    

#1. Pestaña resumen
with pestaña_empresa:
    st.header("Análisis de Rentabilidad por Industria")
    