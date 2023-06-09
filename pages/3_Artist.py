import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("C:/Users/irefu/OneDrive/Documentos/SpotifyApp/dataviz.csv")
st.set_page_config(page_title="Artists", page_icon="🔝")
st.set_option('deprecation.showPyplotGlobalUse', False)

tab1, tab2 = st.tabs(["Top Artist", "Top Songs"])
with tab1:
    # Obtener los años únicos en el dataset
    unique_years = sorted(data['year'].unique())
    unique_years.remove(1998)

    # Obtener el rango de años seleccionado por el usuario
    start_year = st.selectbox('Select initial year', unique_years)
    end_year = st.selectbox('Select final year', unique_years)

    # Obtener el top N de actores populares seleccionado por el usuario
    top_n = st.selectbox('Select top N of actor', [10, 20])

    # Filtrar el dataset por rango de años
    filtered_df = data[(data['year'] >= start_year) & (data['year'] <= end_year)]

    # Obtener el top N de actores populares
    top_actors = filtered_df.groupby('artist')['popularity'].mean().nlargest(top_n)

    # Crear el diagrama de barras
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_actors.values, y=top_actors.index, palette='viridis')
    plt.xlabel('Popularity')
    plt.ylabel('Name of the artist')
    plt.title(f'Top {top_n} Popular Artist between ({start_year}-{end_year})')
    st.pyplot()
    

with tab2:
        # Obtener los 10 actores más populares
    top_actors = data['artist'].value_counts().nlargest(10)

    # Obtener el actor seleccionado por el usuario
    selected_actor = st.selectbox('Select an artist', top_actors.index)

    # Filtrar el dataset por el actor seleccionado
    filtered_df = data[data['artist'] == selected_actor]

    # Obtener el número de canciones populares por año
    songs_by_year = filtered_df.groupby('year')['song'].count().reset_index()


    # Crear el gráfico de líneas
    fig = px.line(songs_by_year, x='year', y='song', title=f'Number of popular songs per year - {selected_actor}')
    fig.update_xaxes(title='Year')
    fig.update_yaxes(title='Number of popular songs')

    st.plotly_chart(fig)


