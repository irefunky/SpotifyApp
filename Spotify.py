import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

data=pd.read_csv("dataviz.csv")
st.set_page_config(page_title="Spotify", page_icon="🎶")
#st.sidebar.image("C:/Users/irefu/OneDrive/Documentos/SpotifyApp/logo.jpeg", use_column_width=True)
st.image("logo.png", width=100)
st.write("# Welcome to our Spotify Analysis! 🎶")
#st.sidebar.success("Select a demo above.")

st.markdown(
        """
        Get ready to get a closer look on your favorite artists and their songs. 
        This dataset containing the 2000 most popular songs in the history of Spotify 
        will give you all your answers.
        


        **👈 Look at the dropdown menu on the left** and feel free to navigate through all of them!

        Want to know what we are talking about?

        Check the introduction page and then you will have more information of the type of data we are working with 

        ### Enjoy your analysis!!🤗""" )

