import streamlit as st
import plotly.express as px
from Carga_datos import cargar_limpiar_datos as cld

def geografia():
    
    #Llamamos la funcion cargar_limpiar_datos as cld del archivo Cargar_datos
    data_geo = cld()

    #agrupamos los datos de paises y salarios, y despues calculamos
    estadistica_geografia = data_geo.groupby('location')['salary_usd'].agg(['mean', 'count']).reset_index()

    #renombramos las columnas
    estadistica_geografia.columns = ['Ubicacion', 'Salario promedio (USD)', 'Cantidad de ofertas']

    st.dataframe(estadistica_geografia.style.format({
        'Salario promedio (USD)': '{:,.2f}'}), use_container_width=True)

    st.divider()

    #mostramos la columna
    top_ciudades = estadistica_geografia.sort_values('Cantidad de ofertas', ascending=False).head(10)

    # Creamos dos columnas para mostrar la info
    columna_oferta, columna_promedio = st.columns(2)

    #Esta columna nos permitira ver la cantidad de demanda laboral por pais
    with columna_oferta:
        st.write("### Demanda laboral")
        fig_ofertas = px.bar(
            top_ciudades,
            x='Cantidad de ofertas',
            y='Ubicacion',
            orientation='h',
            color='Cantidad de ofertas',
            color_continuous_scale='Blues',
            title="Demanda Laboral por Ciudad"
        )
        st.plotly_chart(fig_ofertas, use_container_width=True)

    #Este grafico veremos el salario promedio por pais
    with columna_promedio:
        st.write("### Salario laboral Promedio")
        fig_salarios = px.bar(
            top_ciudades,
            x='Salario promedio (USD)',
            y='Ubicacion',
            orientation='h',
            color='Salario promedio (USD)',
            color_continuous_scale='Greens',
            title="Remuneración por Ciudad"
        )
        st.plotly_chart(fig_salarios, use_container_width=True)

    st.divider()

    st.subheader("Conclusiones del Análisis")
    st.info("informacion")