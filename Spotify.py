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
        In this app you can find different information about artist and songs that were in Spotify. 
        This dataset is based in some characteristics that will help us to know more about songs, 
        the most common genre, its popularity, etc.


        **👈 Select a visualization from the dropdown on the left** to see some examples!

        ### Want to know what we are talking about?

        - Check the introduction page and then you will have more information of the type of data we are working with 

        ### Enjoy your analysis!!🤗""" )

