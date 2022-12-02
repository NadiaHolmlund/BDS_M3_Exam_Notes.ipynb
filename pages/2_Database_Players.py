import streamlit as streamlit


col1, col2 = st.columns(2)

with col1:
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
   
if st.button('Compare players'):

    with col2:
        st.metric(label="Temperature", value="70 °F", delta="1.2 °F")