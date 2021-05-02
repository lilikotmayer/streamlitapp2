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

st.title("Covid-19 app")
st.write("Lili's first working app")

country_select = st.selectbox('Select a country',data['country'].unique())
st.write(f'The selected country is {country_select}')

selected_country = data[data['country']==country_select]
fig = px.line(data_frame = selected_country, x = 'week', y = 'cumulative_count', color = 'indicator')

st.plotly_chart(fig)
