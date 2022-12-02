import streamlit as st

col1, col2 = st.columns(2)

with col1:
    metric("Temperature", "70 °F", "1.2 °F")
    metric("Wind", "9 mph", "-8%")
    metric("Humidity", "86%", "4%")