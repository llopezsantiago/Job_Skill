import streamlit as st #libreria para hacer el dashboard
import pandas as pd #libreria para tratar el database

# esta linea evita que streamlit guarde los datos en cache y no los lea nuevamente
@st.cache_data

#creamos una funcion para cargar el archivo 10. Job y Skills.csv
def cargar_limpiar_datos():
    df = pd.read_csv("10. Job y Skills.csv")
    
    #1.Limpieza: Eliminas filas duplicadas, el drop_duplicates evita contar dos veces el mismo empleo
    df = df.drop_duplicates()

    #2. Limpieza: manejo de valores nulos (vacios)
    #2,1. Limpieza: si falta un dato de salario, dropna elimina la fila donde falta informacion critica
    df = df.dropna(subset=['salary_usd'])

    #2,2. Limpieza: si falta la habilidad, fillna rellena huecos con texto por defecto como "no especificado"
    df['skills_required'] = df['skills_required'].fillna("Skills no especificado") 

    #4 Limpieza: astype cambia el formato de los datos, en este caso a enteros
    df['salary_usd'] = df['salary_usd'].astype(int)

    #A la izquierda creamos una variable donde gurdaremos el resultado
    #a la derecha colocamos la funcion to_datatime para tranformar el archivo a fecha 
    df['posting_date'] = pd.to_datetime(df['posting_date'])

    return df


