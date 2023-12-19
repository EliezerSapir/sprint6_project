import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Exploration of car sales over the years')
# wanted to add , divider='rainbow'

st.subheader('Model Year vs Price')
st.write('Older cars and newer cars sell for the highest price. Car models from 1974-2013 sell on average for less than 15K dollars.')

year = px.histogram(df, df.model_year, df.price, histfunc='avg')

#st.bar_chart(year)
st.plotly_chart(year)

st.subheader('Car Condition vs Price')
st.write('The graph below supports common sense, the new cars sell for the most while the fair and salvage categories consistently sell for the least.')

condition = px.histogram(df, df.condition, df.price, histfunc='avg')

#st.bar_chart(condition)
st.plotly_chart(condition)

st.subheader('Model Year vs Price based on Car Condition')
st.write('The graph below takes this observation deeper, plotting price against model year, with colors marking the condition. We can see from this graph that the majority of cars in new condition were produced in the last 20 years. We can also easily see the outlier with the highest sale was from a car in good condition from 1999.')

fig = px.scatter(df, x="model_year", y="price", color='condition')

#st.scatter_chart(fig)
st.plotly_chart(fig)

st.subheader('What can you expect to pay for a car from the year (in $):')
choice = st.checkbox('1960')
if choice:
    st.write(round(df[df['model_year'] == 1960]['price'].mean()))
choice2 = st.checkbox('1970')
if choice2:
    st.write(round(df[df['model_year'] == 1970]['price'].mean()))
choice3 = st.checkbox('1980')
if choice3:
    st.write(round(df[df['model_year'] == 1980]['price'].mean()))
choice4 = st.checkbox('1990')
if choice4:
    st.write(round(df[df['model_year'] == 1990]['price'].mean()))
choice5 = st.checkbox('2000')
if choice5:
    st.write(round(df[df['model_year'] == 2000]['price'].mean()))
choice6 = st.checkbox('2010')
if choice6:
    st.write(round(df[df['model_year'] == 2010]['price'].mean()))
choice7 = st.checkbox('2019')
if choice7:
    st.write(round(df[df['model_year'] == 2019]['price'].mean()))

year = st.slider('Check a specific year', 1960, 2019, 1960)

st.write('You can expect to pay $', round(df[df['model_year'] == year]['price'].mean()), 'for a car from', year)