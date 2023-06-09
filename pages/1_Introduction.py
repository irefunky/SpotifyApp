import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/irefu/OneDrive/Documentos/SpotifyApp/dataviz.csv")
st.set_page_config(page_title="Introduction", page_icon="📈")
#st.sidebar.image("C:/Users/irefu/OneDrive/Documentos/SpotifyApp/logo.jpeg", use_column_width=True)
st.markdown("# Introduction to Spotify Dataset")
st.markdown('Here you have a datatable that shows the dataset we will be working with.')
st.dataframe(data)