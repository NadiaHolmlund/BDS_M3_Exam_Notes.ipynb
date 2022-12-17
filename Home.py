# Imports
import streamlit as st
import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)

# Before loading the data, we specify page configurations.
# Page_title and page_icon determines the layout of the webbrowser-tab.
# Layout determines the overall layout of the page. Wide specifies that the whole screen width is used for displaying the app.
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide")

st.markdown("<h1 style='text-align: center; color: grey;'>Intelligent Scouting & Player Rating</h1>", unsafe_allow_html=True)
st.write('')

from PIL import Image

col1, col2 = st.columns(2)

with col1:
    picture_1 = Image.open('blog-Pitchero_2-768x384-modified.png')
    st.image(picture_1)

with col2:
    st.write('')
    st.subheader("Player Rating")
    st.write("Feature presentation")
    st.write("Feature presentation")
    demo_1 = st.button('Demo', key='demo_1')
if demo_1:
        video_file = open('/work/M3/Images/Screen Recording 2022-12-04 at 18.26.48.mov', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        close_demo_1 = st.button('Close Demo', key='close_demo_1')




col1, col2 = st.columns(2)

with col1:
    picture_1 = Image.open('/work/M3/Images/blog-Pitchero_2-768x384-modified.png')
    st.image(picture_1)

with col2:
    st.write('')
    st.subheader("Player Comparison")
    st.write("Feature presentation")
    st.write("Feature presentation")
    demo_2 = st.button('Demo', key='demo_2')
if demo_2:
        video_file = open('/work/M3/Images/Screen Recording 2022-12-04 at 18.26.48.mov', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        close_demo_2 = st.button('Close Demo', key='close_demo_2')





col1, col2 = st.columns(2)

with col1:
    picture_1 = Image.open('/work/M3/Images/blog-Pitchero_2-768x384-modified.png')
    st.image(picture_1)

with col2:
    st.write('')
    st.subheader("Player Database")
    st.write("Feature presentation")
    st.write("Feature presentation")
    demo_3 = st.button('Demo', key='demo_3')
if demo_3:
        video_file = open('/work/M3/Images/Screen Recording 2022-12-04 at 18.26.48.mov', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        close_demo_3 = st.button('Close Demo', key='close_demo_3')