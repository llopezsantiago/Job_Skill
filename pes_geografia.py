import streamlit as st
import plotly.express as px
from Carga_datos import cargar_limpiar_datos as cld

def geografia():
    
    #Llamamos la funcion cargar_limpiar_datos as cld del archivo Cargar_datos
    data = cld()

    #------Filtro de interfaz-------
    #Aqui obtenemos una lista unica de las industrias del dataset
    #usamos unique() para contar y tolist() para verlo como lista
    lista_industria = data['industry'].unique().tolist()
    #Aqui obtenemos una lista unica de los paises del dataset
    lista_pais = data['location'].unique().tolist()

    #creamos el componente visual en la barra de lateral
    #sidebar es para crear la barra lateral y multiselect para multiples opciones

    seleccion_Industria = st.sidebar.multiselect(
        "Filtrar por Industria:",
        options=lista_industria,
        default=lista_industria[:1] #permite dejar n primeras marcas al inicio
    )

    seleccion_pais = st.sidebar.multiselect(
        "Filtrar por pais:",
        options=lista_pais,
        default=lista_pais[:2] #permite dejar n primeras marcas al inicio
    )

    #creamos una varible data_filtrada donde solo mostrara los datos filtrados que el usuario eligio
    data_filtrado_general = data[
        (data['industry'].isin(seleccion_Industria)) &
        (data['location'].isin(seleccion_pais))
    ]

    if not data_filtrado_general.empty:
        st.success(f"✅ Se encontraron {len(data_filtrado_general)} vacantes que coinciden con tu búsqueda.")
        # Aquí irían tus métricas y gráficos usando 'data_unificada'
    else:
        st.error("🚫 No hay vacantes para esa combinación de industria y país. Intenta cambiar los filtros.")
        # Esto imprimirá en la página cuántas filas tiene tu filtro actual
        st.write(f"Filas encontradas: {len(data_filtrado_general)}")

    if not data_filtrado_general.empty:
        
        st.subheader("Analisis de Salario")
    
        # Creamos dos columnas
        col1, col2 = st.columns(2)

        # En la primera columna ponemos el total de vacantes
        with col1:
            total_vacantes = len(data_filtrado_general)
            st.metric(label="Total de Vacantes 📋", value=total_vacantes)

        # En la segunda columna ponemos el salario promedio
        with col2:
            # Calculamos el promedio y lo formateamos con signo de pesos
            promedio_salarial = data_filtrado_general['salary_usd'].mean()
            st.metric(label="Salario Promedio 💰", value=f"${promedio_salarial:,.0f} USD")
    
        st.divider()
    
        #agrupamos los datos para que el grafico no se sature
        df_resumen = data_filtrado_general.groupby(['job_title','location'])['salary_usd'].mean().reset_index()

        #ordenamos del mayor salario al menor salario
        df_resumen = df_resumen.sort_values('salary_usd', ascending=False)

        #creamos un grafico de barras simple con plotly
        #x: los datos horizontales
        #y: los datos verticales

        fig = px.bar(
            df_resumen,
            x='job_title',
            y='salary_usd',
            title="Salario promedio por puesto en las industrias seleccionadas",
            labels={'salary_usd': 'Salario promedio (USD)', 'job_title': 'Puesto'},
            color='location', #el color cambia segun el pais
            barmode='group',
            #color_continuous_scale='Blues' #escala de color profesional
        )

        #Mostramos el grafico en pantalla con la versión actualizada para evitar el mensaje de advertencia
        st.plotly_chart(fig, on_select="ignore", selection_mode="points")

    else:
        #mesnaje para indicar al usuario que marque una opcion
        st.warning("Por favor, marque al menos una casilla en el menu lateral para analizar")
