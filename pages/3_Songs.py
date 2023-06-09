import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("dataviz.csv")
st.set_page_config(page_title="Songs&Genre", page_icon="🎧")
tab1, tab2 = st.tabs(["Songs by duration", "Top 5 genre"])
with tab1:
    st.title("People prefer long or short songs?")
    # Obtener el rango de duración en minutos
    min_duration = int(data['duration_min'].min())  # Convertir a entero
    max_duration = int(data['duration_min'].max())  # Convertir a entero

    # Obtener los valores mínimo y máximo seleccionados por el usuario usando un slider con dos handles
    selected_duration_range = st.slider('Select a range of duration in minutes', min_value=min_duration, max_value=max_duration, value=(min_duration, max_duration))

    # Obtener el valor mínimo y máximo del rango seleccionado
    selected_min_duration = selected_duration_range[0]
    selected_max_duration = selected_duration_range[1]

    # Filtrar el dataset por el rango de duración seleccionado
    filtered_df = data[(data['duration_min'] >= selected_min_duration) & (data['duration_min'] <= selected_max_duration)]

    # Agrupar el número de canciones por años
    songs_count_by_year = filtered_df.groupby('year').size().reset_index(name='Count')

    # Calcular el rango de tamaños para los círculos
    size_min = songs_count_by_year['Count'].min()
    size_max = songs_count_by_year['Count'].max()
    size_range = size_max - size_min

    # Ajustar el rango de tamaños de los círculos para hacer la diferencia más notable
    size_scale = 5 + (size_range * 0.4)

    # Crear el gráfico de dispersión utilizando Plotly
    fig = px.scatter(songs_count_by_year, x='year', y='Count', size='Count', size_max=size_scale)
    fig.update_traces(marker=dict(color='steelblue', line=dict(color='white', width=0.5)))
    fig.update_layout(title='Number of songs per year',
                    xaxis_title='Year',
                    yaxis_title='Number of songs')

    # Mostrar el gráfico interactivo utilizando st.plotly_chart
    st.plotly_chart(fig)
with tab2:
        # Add a title
    st.title("Is your favorite genre in the list?")

    # Agregar un selectbox para seleccionar el año
    unique_years = sorted(data['year'].unique())
    unique_years.remove(1998)
    year = st.selectbox("Select a year:", unique_years)

    # Filtrar los datos basándose en el año seleccionado
    filtered_data = data[data["year"] == year ]
    filtered_data = filtered_data[filtered_data['genre']!= "set()"]
    # Calcular los géneros más repetidos
    top_genres = filtered_data["genre"].value_counts().head(5).reset_index()
    top_genres.columns = ["Genre", "Count"]

    # Calcular el porcentaje de cada género
    top_genres["Percentage"] = top_genres["Count"] / top_genres["Count"].sum() * 100

    # Crear el gráfico de tipo pie chart utilizando Plotly
    fig = px.pie(top_genres, values='Count', names='Genre', 
                title=f"Top 5 Genres in {year} (Percentage)")

    # Mostrar el gráfico interactivo utilizando st.plotly_chart
    st.plotly_chart(fig)