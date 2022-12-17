# Imports
import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import shap
from streamlit_shap import st_shap
import pickle
import plotly.graph_objects as go
fig = go.Figure()
fig.update_layout(margin=dict(l=25, r=25, t=25, b=25), polar=dict(radialaxis=dict(visible=True, range=[0, 100])),showlegend=False)

# Setting up page configurations
st.set_page_config(
    page_title="Player Rating",
    page_icon="👤",
    layout="wide")

# Expanding the width of the sidebar (to fit feature names in one line in the sidebar)
st.markdown(
"""<style>[data-testid="stSidebar"][aria-expanded="true"] > div:first-child {width: 400px;}
[data-testid="stSidebar"][aria-expanded="false"] > div:first-child {width: 400px;}
</style>""",unsafe_allow_html=True)





# Loading data, models, scalers, explainers, etc., only once
@st.experimental_singleton
def read_objects():
    BL = pd.read_csv('/work/M3/Pickles/0_Data/BL.csv')

    # Model, scaler, explainer and features selected for each position
    GK_model = pickle.load(open('/work/M3/Pickles/1_GK/GK_model.pkl','rb'))
    GK_scaler = pickle.load(open('/work/M3/Pickles/1_GK/GK_scaler.pkl','rb'))
    GK_shap_values = pickle.load(open('/work/M3/Pickles/1_GK/GK_shap.pkl','rb'))
    GK_rmse  = pickle.load(open('/work/M3/Pickles/1_GK/GK_rmse.pkl','rb'))
    GK_explainer = shap.TreeExplainer(GK_model)
    GK_fs = pd.read_csv('/work/M3/Pickles/1_GK/GK_fs.csv')

    return BL, GK_model, GK_scaler, GK_shap_values, GK_rmse, GK_explainer, GK_fs

BL, GK_model, GK_scaler, GK_shap_values, GK_rmse, GK_explainer, GK_fs = read_objects()





# Setting up the default sidebar
player = st.sidebar.text_input((''),('Player'))
col1, col2 = st.sidebar.columns(2)
team = col1.text_input((''),('Team'))
age = col1.text_input((''),('Age'))
weight = col1.text_input((''),('Weight'))
foot = col2.selectbox((''),('Foot', 'Right', 'Left', 'Both', 'Unknown'))
height = col2.text_input((''),('Height'))
nationality = col2.text_input((''),('Nationality'))
position = st.sidebar.selectbox((''),('Position', 'Goalkeeper', 'Central Defender', 'Full Back', 'Defensive Midfielder', 'Central Midfielder', 'Attacking Midfielder', 'Winger Midfielder', 'Forwarder'))




# Setting up the default page
if position == 'Position':

    # Setting up the default page
    col1, col2 = st.columns([2, 3])

    # Adding user input from the sidebar to the default page     
    if player == 'Player': col1.header('Player')
    else: col1.header(player)
    if position == 'Position': col1.info('Position:  ')
    else: col1.info('Position:  ' + position)
    if team == 'Team': col1.info('Team:  ')
    else: col1.info('Team:  ' + team)
    if foot == 'Foot': col1.info('Foot:  ')
    else: col1.info('Foot:  ' + foot)
    if age == 'Age': col1.info('Age:  ')
    else: col1.info('Age:  ' + age)
    if height == 'Height': col1.info('Height:  ')
    else: col1.info('Height:  ' + height)
    if weight == 'Weight': col1.info('Weight:  ')
    else: col1.info('Weight:  ' + weight)

    # Setting up the default radar graph
    col2.write('')
    col2.write('')
    categories = ['Feature 0', 'Feature 1', 'Feature 2','Feature 3','Feature 4','Feature 5','Feature 6','Feature 7','Feature 8', 'Feature 9']
    fig.add_trace(go.Scatterpolar(r=[50, 50, 50, 50, 50, 50, 50, 50, 50, 50], theta=categories, fill='toself', name=player))
    col2.plotly_chart(fig, use_container_width=True)

    # Setting up the rest of the default page
    col1, col2, col3, col4, col5, col6= st.columns([2, 0.8, 1, 0.1, 1, 0.1])

    # Adding user input from the sidebar to the default page
    if nationality == 'Nationality': col1.info('Nationality:  ')
    else: col1.info('Nationality:  ' + nationality)

    # Setting up the rest of the default page
    col3.metric(label="Player Rating", value='00.0')
    col4.write('')
    col5.metric(label="Mean Error", value='00.0')
    col6.write('')
    with st.expander("Player Rating Explained"):
        st.write('')





# Setting up the page for position GK
if position == 'Goalkeeper':

    # Setting up the sidebar
    col1, col2 = st.sidebar.columns(2)
    feature_0 = col1.number_input((GK_fs.iloc[0].values[0]), key=0, min_value=0, step=10)
    feature_2 = col1.number_input((GK_fs.iloc[2].values[0]), key=2, min_value=0, step=10)
    feature_4 = col1.number_input((GK_fs.iloc[4].values[0]), key=4, min_value=0, step=10)
    feature_6 = col1.number_input((GK_fs.iloc[6].values[0]), key=6, min_value=0, step=10)
    feature_8 = col1.number_input((GK_fs.iloc[8].values[0]), key=8, min_value=0, step=10)
    
    feature_1 = col2.number_input((GK_fs.iloc[1].values[0]), key=1, min_value=0, step=10)
    feature_3 = col2.number_input((GK_fs.iloc[3].values[0]), key=3, min_value=0, step=10)
    feature_5 = col2.number_input((GK_fs.iloc[5].values[0]), key=5, min_value=0, step=10)
    feature_7 = col2.number_input((GK_fs.iloc[7].values[0]), key=7, min_value=0, step=10)
    feature_9 = col2.number_input((GK_fs.iloc[9].values[0]), key=9, min_value=0, step=10)

    compare_BL = st.sidebar.checkbox('Compare ' + player + ' to the highest rated ' + position + ' in the Bundesliga')

    # Setting up the page
    col1, col2 = st.columns([2, 3])

    # Adding user input from the sidebar to the page
    if player == 'Player': col1.header('Player')
    else: col1.header(player)
    if position == 'Position': col1.info('Position:  ')
    else: col1.info('Position:  ' + position)
    if team == 'Team': col1.info('Team:  ')
    else: col1.info('Team:  ' + team)
    if foot == 'Foot': col1.info('Foot:  ')
    else: col1.info('Foot:  ' + foot)
    if age == 'Age': col1.info('Age:  ')
    else: col1.info('Age:  ' + age)
    if height == 'Height': col1.info('Height:  ')
    else: col1.info('Height:  ' + height)
    if weight == 'Weight': col1.info('Weight:  ')
    else: col1.info('Weight:  ' + weight)

    # Setting up the radar graph
    col2.write('')
    col2.write('')
    categories =    [GK_fs.iloc[0],
                    GK_fs.iloc[1],
                    GK_fs.iloc[2],
                    GK_fs.iloc[3],
                    GK_fs.iloc[4],
                    GK_fs.iloc[5],
                    GK_fs.iloc[6],
                    GK_fs.iloc[7],
                    GK_fs.iloc[8],
                    GK_fs.iloc[9]]
    fig.add_trace(go.Scatterpolar(r=    [(feature_0 - 0) / (BL[GK_fs.iloc[0].values[0]].max() - 0) * 100,
                                        (feature_1 - 0) / (BL[GK_fs.iloc[1].values[0]].max() - 0) * 100,
                                        (feature_2 - 0) / (BL[GK_fs.iloc[2].values[0]].max() - 0) * 100,
                                        (feature_3 - 0) / (BL[GK_fs.iloc[3].values[0]].max() - 0) * 100,
                                        (feature_4 - 0) / (BL[GK_fs.iloc[4].values[0]].max() - 0) * 100,
                                        (feature_5 - 0) / (BL[GK_fs.iloc[5].values[0]].max() - 0) * 100,
                                        (feature_6 - 0) / (BL[GK_fs.iloc[6].values[0]].max() - 0) * 100,
                                        (feature_7 - 0) / (BL[GK_fs.iloc[7].values[0]].max() - 0) * 100,
                                        (feature_8 - 0) / (BL[GK_fs.iloc[8].values[0]].max() - 0) * 100,
                                        (feature_9 - 0) / (BL[GK_fs.iloc[9].values[0]].max() - 0) * 100
                                        ],theta=categories, fill='toself', name=player))

    if compare_BL:
        feature_0_BL = BL[GK_fs.iloc[0].values[0]].loc[(BL['Position'] == 'GK') & (BL['Rating'] == BL['Rating'].max())].values[0]
        feature_1_BL = BL[GK_fs.iloc[1].values[0]].loc[(BL['Position'] == 'GK') & (BL['Rating'] == BL['Rating'].max())].values[0]
        feature_2_BL = BL[GK_fs.iloc[2].values[0]].loc[(BL['Position'] == 'GK') & (BL['Rating'] == BL['Rating'].max())].values[0]
        feature_3_BL = BL[GK_fs.iloc[3].values[0]].loc[(BL['Position'] == 'GK') & (BL['Rating'] == BL['Rating'].max())].values[0]
        feature_4_BL = BL[GK_fs.iloc[4].values[0]].loc[(BL['Position'] == 'GK') & (BL['Rating'] == BL['Rating'].max())].values[0]
        feature_5_BL = BL[GK_fs.iloc[5].values[0]].loc[(BL['Position'] == 'GK') & (BL['Rating'] == BL['Rating'].max())].values[0]
        feature_6_BL = BL[GK_fs.iloc[6].values[0]].loc[(BL['Position'] == 'GK') & (BL['Rating'] == BL['Rating'].max())].values[0]
        feature_7_BL = BL[GK_fs.iloc[7].values[0]].loc[(BL['Position'] == 'GK') & (BL['Rating'] == BL['Rating'].max())].values[0]
        feature_8_BL = BL[GK_fs.iloc[8].values[0]].loc[(BL['Position'] == 'GK') & (BL['Rating'] == BL['Rating'].max())].values[0]
        feature_9_BL = BL[GK_fs.iloc[9].values[0]].loc[(BL['Position'] == 'GK') & (BL['Rating'] == BL['Rating'].max())].values[0]

        fig.add_trace(go.Scatterpolar(r=    [(feature_0_BL - 0) / (BL[GK_fs.iloc[0].values[0]].max() - 0) * 100,
                                            (feature_1_BL - 0) / (BL[GK_fs.iloc[1].values[0]].max() - 0) * 100,
                                            (feature_2_BL - 0) / (BL[GK_fs.iloc[2].values[0]].max() - 0) * 100, 
                                            (feature_3_BL - 0) / (BL[GK_fs.iloc[3].values[0]].max() - 0) * 100, 
                                            (feature_4_BL - 0) / (BL[GK_fs.iloc[4].values[0]].max() - 0) * 100, 
                                            (feature_5_BL - 0) / (BL[GK_fs.iloc[5].values[0]].max() - 0) * 100, 
                                            (feature_6_BL - 0) / (BL[GK_fs.iloc[6].values[0]].max() - 0) * 100, 
                                            (feature_7_BL - 0) / (BL[GK_fs.iloc[7].values[0]].max() - 0) * 100, 
                                            (feature_8_BL - 0) / (BL[GK_fs.iloc[8].values[0]].max() - 0) * 100, 
                                            (feature_9_BL - 0) / (BL[GK_fs.iloc[9].values[0]].max() - 0) * 100,
                                            ], theta=categories, fill='toself', name=BL.loc[(BL['Position'] == 'GK') & (BL['Rating'] == BL['Rating'].max()), 'Player'].values[0]))

    # Plotting the graph
    col2.plotly_chart(fig, use_container_width=True)

    # Setting up the rest of the page
    col1, col2, col3, col4, col5, col6= st.columns([2, 0.8, 1, 0.1, 1, 0.1])

    # Adding user input from the sidebar to the page
    if nationality == 'Nationality': col1.info('Nationality:  ')
    else: col1.info('Nationality:  ' + nationality)
    col2.write('')

    # Adding a button that triggers prediction of the rating
    if st.sidebar.button('Predict Player Rating'):
        st.sidebar.write('')
        st.sidebar.write('')
        # Creating a dataframe with feature names and user input from the sidebar
        user_input = pd.DataFrame({ GK_fs.iloc[0].values[0]:feature_0,
                                    GK_fs.iloc[1].values[0]:feature_1, 
                                    GK_fs.iloc[2].values[0]:feature_2, 
                                    GK_fs.iloc[3].values[0]:feature_3, 
                                    GK_fs.iloc[4].values[0]:feature_4, 
                                    GK_fs.iloc[5].values[0]:feature_5,
                                    GK_fs.iloc[6].values[0]:feature_6,                                         
                                    GK_fs.iloc[7].values[0]:feature_7, 
                                    GK_fs.iloc[8].values[0]:feature_8, 
                                    GK_fs.iloc[9].values[0]:feature_9, 
                                    }, index=[0]) 
        # Scaling the user input
        user_input_scaled = pd.DataFrame(GK_scaler.transform(user_input), columns = user_input.columns, index=[0])  

        # Predicting the rating based on the user input
        predicted_rating = GK_model.predict(user_input_scaled)
    
        # Displaying the rating and RMSE
        col3.metric(label="Player Rating", value=np.round(predicted_rating, decimals = 2))
        col4.write('')
        col5.metric(label="Mean Error", value=np.round(GK_rmse, decimals = 2))
        col6.write('')

        # Displaying the SHAP values
        with st.expander("Player Rating Explained"):
            shap_value = GK_explainer.shap_values(user_input_scaled)
            st_shap(shap.force_plot(GK_explainer.expected_value, shap_value, user_input_scaled), height=150, width=700)
    
    # Default display when the button has not been pressed
    else:
        st.sidebar.write('')
        st.sidebar.write('')
        col3.metric(label="Player Rating", value='00.0')
        col4.write('')
        col5.metric(label="Mean Error", value='00.0')
        col6.write('')
        with st.expander("Player Rating Explained"):
            st.write('')