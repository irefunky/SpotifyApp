import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("dataviz.csv")
st.set_page_config(page_title="Artists", page_icon="🔝")
st.set_option('deprecation.showPyplotGlobalUse', False)

tab1, tab2 = st.tabs(["Top Artist", "Top Songs"])
with tab1:
    st.title("Greatest artists along the years")

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
    top_actors = filtered_df.groupby('artist')['popularity'].mean().nlargest(top_n).reset_index()

    # Crear el diagrama de barras con Plotly
    fig = px.bar(top_actors, x='popularity', y='artist', orientation='h', color='popularity',
                color_continuous_scale='viridis', title=f'Top {top_n} Popular Artist between ({start_year}-{end_year})',
                category_orders={'artist': top_actors['artist'].values[::]})
    # Mostrar el gráfico utilizando Streamlit
    st.plotly_chart(fig)

    

with tab2:
    st.title("How many songs an artist has?")
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


