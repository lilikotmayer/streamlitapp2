import streamlit as st 
import pandas as pd 
import plotly.express as px

@st.cache
def load_data():
    data = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv')
    data['week'] = data.year_week.apply(lambda x: convert(x))
    return data

def convert(x):
    year, week = x.split('-')
    year = (int(year) - 2020) * 52
    return year + int(week)

data = load_data()

hun = data[data.country == 'Hungary']
fig = px.line(data_frame = hun, x = 'week', y = 'cumulative_count', color = 'indicator')


st.write("Again! 3x")
st.title("Hello World")

country = st.selectbox('Select a country', ['Hungary', 'Belgium'])
st.write(f'The selected country is {country}')

st.plotly_chart(fig)

st.write(fig)