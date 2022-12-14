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
    name = st.text_input('Name')
    st.selectbox(('League'),('Bundesliga', 'Superliga'))
    position = st.selectbox(('Position'),('GK', 'DF', 'MF', 'FW'))
    st.slider('Age', 15, 45, 30)
    metric_1 = st.slider('Metric 1', 0, 100, 50)
    metric_2 = st.slider('Metric 2', 0, 100, 50)
    metric_3 = st.slider('Metric 3', 0, 100, 50)
    metric_4 = st.slider('Metric 4', 0, 100, 50)
    metric_5 = st.slider('Metric 5', 0, 100, 50)
    st.button('Assess Player')




import plotly.graph_objects as go


categories = ['Metric 1','Metric 2','Metric 3',
              'Metric 4', 'Metric 5']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[metric_1, metric_2, metric_3, metric_4, metric_5],
      theta=categories,
      fill='toself',
      name='Product A'
))
fig.add_trace(go.Scatterpolar(
      r=[4, 3, 2.5, 1, 2],
      theta=categories,
      fill='toself',
      name='Product B'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 100]
    )),
  showlegend=False
)

# Plot!
st.plotly_chart(fig, use_container_width=True)

compare = st.checkbox('Compare with highest rated player based on position')









import streamlit as st
from PIL import Image

image_gk = Image.open('app_images/GK.png')
image_df = Image.open('app_images/DF.png')
image_mf = Image.open('app_images/MF.png')
image_fw = Image.open('app_images/FW.png')


if position == 'GK':
    st.image(image_gk, 'Position')
elif position == 'DF':
    st.image(image_df, 'Position')
elif position == 'MF':
    st.image(image_mf, 'Position')
elif position == 'FW':
    st.image(image_fw, 'Position')
