import streamlit as st
import pandas as pd
import plotly.express as px
from Carga_datos import cargar_limpiar_datos as cld

def salario():
    
    #Llamamos la funcion cargar_limpiar_datos as cld del archivo Cargar_datos
    data_sal = cld()

    st.subheader("Estadistica descriptiva del salario en las industrias")

    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        promedio_total = data_sal['salary_usd'].mean()
        st.metric("Promedio Global", f"{promedio_total:,.2f} USD")
        
    with m2:
        mediana_total = data_sal['salary_usd'].median()
        st.metric("Mediana Global", f"{mediana_total:,.2f} USD")
        
    with m3:
        # Calculamos la desviación estándar para ver la variabilidad
        desviacion_total = data_sal['salary_usd'].std()
        st.metric("Desviación Estándar", f"{desviacion_total:,.2f} USD")

    with m4:
        # Calculamos el coeficiente de variacion
        coeficiente_variacion = float(data_sal['salary_usd'].std() / data_sal['salary_usd'].mean()) * 100
        st.metric("Coeficiente de Variación", f"{coeficiente_variacion:,.2f} %")

    st.divider()
    
    #------Tabla de estadistica descriptiva----
    
    st.subheader("Detalle Estadístico por Industria")
    estadisticas_salario = data_sal.groupby('industry')['salary_usd'].agg(['mean', 'median', 'std', lambda x: (x.std() / x.mean()) * 100]).reset_index()
    
    # Creamos las columnas y sus titulos
    estadisticas_salario.columns = ['Industria', 'Promedio (USD)', 'Mediana (USD)', 'Desviación Estándar', 'Coeficiente de Variación (%)']
    
    # Aquí mostramos la tabla que calculaste con .agg()
    st.dataframe(estadisticas_salario.style.format({
        'Promedio (USD)': '{:,.2f}',
        'Mediana (USD)': '{:,.2f}',
        'Desviación Estándar': '{:,.2f}',
        'Coeficiente de Variación (%)': '{:.2f}%'}), use_container_width=True)

    #mensaje informativo sobre cv
    st.info(f"""
    
    1. **Un CV bajo** (ej. < 15%) indica que los salarios en esa industria son muy similares entre sí.
    2. **Un CV alto** (ej. > 30%) sugiere que hay mucha diferencia entre los que ganan poco y los que ganan mucho.
    
    """)

    st.divider()

    df_grafico = estadisticas_salario.sort_values('Promedio (USD)', ascending=False)

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
    # 0.1 es un espacio moderado, 0 es totalmente pegadas
    fig.update_layout(bargap=0.1)
    
    #Mostramos el grafico en pantalla, pero no saldra el mensaje de advertencia
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

    st.divider()
    st.subheader("Conclusiones del Análisis")

    # Extraemos datos para que la conclusión sea inteligente
    industria_max = df_grafico.iloc[0]['Industria']
    salario_max = df_grafico.iloc[0]['Promedio (USD)']

    # Usamos f-strings para insertar los datos en el texto
    st.info(f"""
    **Principales Hallazgos:**

    1. **Líder del Mercado:** La industria de **{industria_max}** presenta el promedio salarial más alto con **${salario_max:,.2f} USD**.
    2. **La estabilidad vs La volatilidad:** hemos observado el Coeficiente de Variación, llegando a la conclusion que  podemos identificar qué sectores tienen sueldos más estandarizados y cuáles presentan brechas más amplias.

    """)
