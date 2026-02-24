import streamlit as st
import pandas as pd
import plotly.express as px
from Carga_datos import cargar_limpiar_datos as cld

def habilidades():
    data_habilidades = cld()

    # 1. Limpieza y preparación (Suponiendo que 'skills_required' es una lista o texto)
    # Si es texto separado por comas, lo convertimos a lista primero
    df_skills = data_habilidades.copy()
    if df_skills['skills_required'].dtype == 'object':
        df_skills['skills_required'] = df_skills['skills_required'].str.split(', ')

    # 2. "Explotamos" las habilidades para tener una por fila
    df_exploded = df_skills.explode('skills_required')

    # 3. Selector de Industria
    industrias = df_exploded['industry'].unique()
    sector_seleccionado = st.selectbox("Selecciona un sector para ver sus habilidades críticas:", industrias)

    # 4. Filtrar y Contar
    df_sector = df_exploded[df_exploded['industry'] == sector_seleccionado]
    conteo_skills = df_sector['skills_required'].value_counts().reset_index()
    conteo_skills.columns = ['Habilidad', 'Frecuencia']

    # 5. Graficar las Top 15
    top_skills = conteo_skills.sort_values('Frecuencia', ascending=True)
    
    fig_bar = px.bar(
        top_skills,
        x='Frecuencia',
        y='Habilidad',
        orientation='h',
        title=f"Top Habilidades en el sector: {sector_seleccionado}",
        color='Frecuencia',
        color_continuous_scale='Blues'
    )
    
    fig_bar.update_layout(boxgap=0.1,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig_bar, use_container_width=True)