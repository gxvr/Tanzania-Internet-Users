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
    'Options', ['2015', '2016', '2017', '2018', '2019', '2020'], key='1')


# Main
image = Image.open('assets/internet.png')
st.image(image, use_column_width=True)

st.title('Tanzania Internet Users Stats')
st.markdown(
    'This application visualize internet penetration statistics in Tanzania from 2015 -2020')


st.title('Facts')
st.subheader('🧑 Internet Users')
st.write('• There were 14.72 million internet users in January 2020.')
st.write('• Internet penetration stood at 25% in January 2020.')
st.write('• Internet users increased by 428 thousand (+3.0%) between 2019 and 2020.')

st.subheader('🚀 Social Media Users')
st.write('• There were 4.50 million social media users in January 2020.')
st.write('• Social media penetration stood at 7.6% in January 2020.')
st.write('• Social media users increased by 514 thousand (+13%)')

st.subheader('📱 Mobile Connections')
st.write('• There were 44.13 million mobile connections in January 2020.')
st.write('• Mobile connections increased by 709 thousand (+1.6%).')
st.write('• Mobile connections in January 2020 was equivalent to 75% of the total population.')


# st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})


# Custom
# hide_footer_style = """
#     <style>
#     .reportview-container .main footer {visibility: hidden;}
#     """
# st.markdown(hide_footer_style, unsafe_allow_html=True)
