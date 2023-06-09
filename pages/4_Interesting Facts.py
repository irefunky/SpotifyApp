import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("dataviz.csv")
st.set_page_config(page_title="Interesting Facts", page_icon="🔍")
st.title('Being elicit is related with popularity?')
# Obtener los géneros únicos en el dataset
unique_genres = data['genre'].unique()

# Obtener el género seleccionado por el usuario
selected_genre = st.selectbox('Select a genre', unique_genres)

# Filtrar el dataset por el género seleccionado
filtered_df = data[data['genre'] == selected_genre]

# Calcular la cantidad de canciones explícitas e implícitas
explicit_counts = filtered_df['explicit'].value_counts()

# Crear el gráfico de barras con Plotly
fig = px.bar(explicit_counts, x=explicit_counts.index, y=explicit_counts.values)

# Configurar las etiquetas de los ejes y el título
fig.update_layout(
    xaxis=dict(title='Explicit', tickmode='array', tickvals=[0, 1], ticktext=['NO', 'YES']),
    yaxis=dict(title='Number of songs'),
    title=f'Distribution of explicit or implicit songs for  ({selected_genre})'
)

# Mostrar el gráfico interactivo utilizando st.plotly_chart
st.plotly_chart(fig)