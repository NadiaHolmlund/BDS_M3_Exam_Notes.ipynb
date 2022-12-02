import streamlit as st

# Before loading the data, we specify page configurations.
# Page_title and page_icon determines the layout of the webbrowser-tab.
# Layout determines the overall layout of the page. Wide specifies that the whole screen width is used for displaying the app.
st.set_page_config(
    page_title="⚽ Homepage",
    page_icon="⚽",
    layout="wide")

st.title("Intelligent Scouting & Player Assessment")
st.sidebar.success("select a page above")
