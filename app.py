import streamlit as st
import pandas as pd
from PIL import Image


# Dataset
# DATA_URL = ('data/')
# data = pd.read_csv(DATA_URL)

# Sidebar
st.sidebar.title('Settings')
st.sidebar.markdown('Interactive Configurations')
st.sidebar.title('Year')
select = st.sidebar.selectbox(
    'Options', ['2015', '2016', '2017', '2018', '2019'], key='1')


# Main
image = Image.open('assets/internet.png')
st.image(image, use_column_width=True)

st.title('Tanzania Internet Users Stats')
st.markdown(
    'This application visualize internet penetration statistics in Tanzania from 2015 -2019')

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})


# Custom
# hide_footer_style = """
#     <style>
#     .reportview-container .main footer {visibility: hidden;}
#     """
# st.markdown(hide_footer_style, unsafe_allow_html=True)
