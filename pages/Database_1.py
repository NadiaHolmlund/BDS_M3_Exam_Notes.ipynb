# Imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Setting up page configurations
st.set_page_config(
    page_title="Database",
    page_icon="📂",
    layout="wide")




with st.sidebar:
    st.radio('League', ('Bundesliga', 'Superliga'))
    st.radio('Year', ('2018', '2019', '2020', '2021', '2022'))
    st.selectbox('Player',('Player', 'Player_2', 'Mobile phone'))