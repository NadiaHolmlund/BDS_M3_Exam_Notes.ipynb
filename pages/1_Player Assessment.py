import streamlit as st

# Before loading the data, we specify page configurations.
# Page_title and page_icon determines the layout of the webbrowser-tab.
# Layout determines the overall layout of the page. Wide specifies that the whole screen width is used for displaying the app.
st.set_page_config(
    page_title="⚽ Player Assessment",
    page_icon="⚽",
    layout="wide")

# Using "with" notation
with st.sidebar:
    st.text_input('Name')
    st.selectbox(('League'),('Bundesliga', 'Superliga'))
    st.selectbox(('Position'),('GK', 'CD', 'MF', 'etc.'))
    st.slider('Age', 15, 45, 1)
    st.slider('Metric 1', 0, 100, 1)
    st.slider('Metric 2', 0, 100, 1)
    st.slider('Metric 3', 0, 100, 1)
    st.slider('Metric 4', 0, 100, 1)
    st.slider('Metric 5', 0, 100, 1)



st.button('Assess Player')
    with st.spinner(text="In progress..."):
        time.sleep(5)
    st.success('Done!')
