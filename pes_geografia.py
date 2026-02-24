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
        'Salario promedio (USD)': '{:,.2f} USD '}), use_container_width=True, )

    st.divider()

    # Creamos dos columnas para mostrar la info
    columna_oferta, columna_promedio = st.columns(2)
    
    #mostramos la columna
    top_ciudades = estadistica_geografia.sort_values('Cantidad de ofertas', ascending=True)

    #Esta columna nos permitira ver la cantidad de demanda laboral por pais
    with columna_oferta:
        st.write("### Demanda laboral")
        fig_ofertas = px.bar(
            top_ciudades,
            x='Cantidad de ofertas',
            y='Ubicacion',
            orientation='h',
            color='Cantidad de ofertas',
            color_continuous_scale=px.colors.sequential.Blues,
            title="Demanda Laboral por Ciudad"
        )
        fig_ofertas.update_yaxes(categoryorder='trace')
        st.plotly_chart(fig_ofertas, use_container_width=True)
        
    #mostramos la columna
    top_promedio = estadistica_geografia.sort_values('Salario promedio (USD)', ascending=True)

    #Este grafico veremos el salario promedio por pais
    with columna_promedio:
        st.write("### Salario laboral Promedio")
        fig_salarios = px.bar(
            top_promedio,
            x='Salario promedio (USD)',
            y='Ubicacion',
            orientation='h',
            color='Salario promedio (USD)',
            color_continuous_scale=px.colors.sequential.Blues,
            title="Remuneración por Ciudad"
        )
        fig_salarios.update_yaxes(categoryorder='trace')
        st.plotly_chart(fig_salarios, use_container_width=True)

    st.divider()

    st.subheader("Conclusiones del Análisis")
    st.info("informacion")