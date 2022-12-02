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
    st.selectbox(('Position'),('GK', 'CD', 'MF', 'etc.'))
    st.slider('Age', 15, 45, 1)
    st.slider('Metric 1', 0, 100, 1)
    st.slider('Metric 2', 0, 100, 1)
    st.slider('Metric 3', 0, 100, 1)
    st.slider('Metric 4', 0, 100, 1)
    st.slider('Metric 5', 0, 100, 1)
    st.button('Assess Player')

st.write(name)








import plotly.graph_objects as go


categories = ['processing cost','mechanical properties','chemical stability',
              'thermal stability', 'device integration']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[1, 5, 2, 2, 3],
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
      range=[0, 5]
    )),
  showlegend=False
)

# Plot!
st.plotly_chart(fig, use_container_width=True)






import plotly
import plotly.graph_objects as go
from PIL import Image

img = Image.open('https://i.stack.imgur.com/zQMZj.png')
fig = go.Figure()

fig.add_trace(
    go.Scatter(x=[0, 110, 112, 114, 115, 130],
               y=[0, 65, 55, 49, 53, 90],
                mode='markers',
                marker=dict(size=15,
                color='red'),
               name='Salah'
))

# axis hide、yaxis reversed
fig.update_layout(
    autosize=False,
    width=1163,
    height=783,
    xaxis=dict(visible=True,autorange=True),
    yaxis=dict(visible=True,autorange='reversed')
)

# background image add
fig.add_layout_image(
    dict(source=img,
         xref='x',
         yref='y',
         x=0,
         y=0,
         sizex=135,
         sizey=95,
         sizing='stretch',
         opacity=0.9,
         layer='below')
)

# Set templates
fig.update_layout(template="plotly_white")

fig.show()