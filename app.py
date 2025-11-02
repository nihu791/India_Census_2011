import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title = 'India Census 2011', page_icon = '🇮🇳', layout = 'wide')

India_census = pd.read_csv('final_df.csv')

list_of_states = India_census['State'].unique().tolist()
list_of_states.insert(0, 'All States')

st.sidebar.title('India Census 2011')

selected_state = st.sidebar.selectbox('Select State', list_of_states)
first_parameter = st.sidebar.selectbox('Select First Parameter', sorted(India_census.columns[5:].tolist()))
second_parameter = st.sidebar.selectbox('Select Second Parameter', sorted(India_census.columns[5:].tolist()))

plot = st.sidebar.button('Plot Map')

if plot:

    st.markdown('''
                - First Parameter represented by Size''')
    st.markdown('''
                - Second Parameter represented by Color''')
    
    if selected_state == 'All States':

        # plot for all states

        fig = px.scatter_mapbox(India_census, lat = 'Latitude', lon = 'Longitude', zoom = 3, hover_name = 'District', hover_data = [first_parameter, second_parameter] ,mapbox_style ='carto-positron', size = first_parameter, color = second_parameter, width = 1400, height = 700, title = f'India Census 2011: {first_parameter} vs {second_parameter} for All States', size_max = 25)

        st.plotly_chart(fig, use_container_width = True)
    else:
        # plot for selected state 
        state_data = India_census[India_census['State'] == selected_state]

        fig = px.scatter_mapbox(state_data , lat = 'Latitude', lon = 'Longitude', zoom = 5, hover_name = 'District', hover_data = [first_parameter, second_parameter] ,mapbox_style ='carto-positron', size = first_parameter, color = second_parameter, width = 1400, height = 700, title = f'India Census 2011: {first_parameter} vs {second_parameter} for {selected_state}', size_max = 25)
        
        st.plotly_chart(fig, use_container_width = True)