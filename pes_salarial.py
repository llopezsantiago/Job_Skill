import streamlit as st
import pandas as pd
import plotly.express as px
from Carga_datos import cargar_limpiar_datos as cld

def salario():
    
    #Llamamos la funcion cargar_limpiar_datos as cld del archivo Cargar_datos
    data_sal = cld()

    m1, m2, m3 = st.columns(3)
    
    with m1:
        promedio_total = data_sal['salary_usd'].mean()
        st.metric("Promedio Global", f"${promedio_total:,.0f} USD")
        
    with m2:
        mediana_total = data_sal['salary_usd'].median()
        st.metric("Mediana Global", f"${mediana_total:,.0f} USD")
        
    with m3:
        # Calculamos la desviación estándar para ver la variabilidad
        desviacion_total = data_sal['salary_usd'].std()
        st.metric("Desviación Estándar", f"${desviacion_total:,.0f} USD")

    st.divider()
    
    estadisticas = data_sal.groupby('industry')['salary_usd'].agg(['mean', 'median', 'std']).reset_index()
    
    # Renombramos para que sea más legible
    estadisticas.columns = ['Industria', 'Promedio (USD)', 'Mediana (USD)', 'Desviación Estándar']

    st.subheader("Detalle Estadístico por Industria")
    # Aquí mostramos la tabla que calculaste con .agg()
    st.dataframe(estadisticas, use_container_width=True)

    st.divider()

    df_grafico = estadisticas.sort_values('Promedio (USD)', ascending=False)

    fig = px.bar(
            df_grafico,
            x='Industria',
            y='Promedio (USD)',
            title="Salario promedio de las industrias",
            labels={'Promedio (USD)': 'Salario Promedio (USD)', 'Industria': 'Sector'},
            color='Industria', #el color cambia segun el pais
            color_discrete_sequence=px.colors.qualitative.Prism
        )
    # Ajustamos el espacio entre las barras (gap)
    # 0.1 es un espacio muy elegante, 0 es totalmente pegadas
    fig.update_layout(bargap=0.1)
    
    #Mostramos el grafico en pantalla con la versión actualizada para evitar el mensaje de advertencia
    st.plotly_chart(fig, on_select="ignore", selection_mode="points")

    st.divider()

    fig_box = px.box(
        data_sal, 
        x='industry', 
        y='salary_usd', 
        color='industry',
        title="Dispersión Salarial: ¿Dónde hay más variedad de sueldos?"
    )
    st.plotly_chart(fig_box)

