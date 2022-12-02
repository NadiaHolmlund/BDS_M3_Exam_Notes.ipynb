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

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.header("Player Assessment")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col1:
        st.header("Player Assessment")
        st.image("https://static.streamlit.io/examples/cat.jpg")