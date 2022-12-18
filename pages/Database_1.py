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
    st.radio('League', 'Bundesliga')