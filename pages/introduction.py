import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
def app():
    st.success('Datasets')
    st.markdown('**This web-app is developed as a part of M.Sc Data Science project (2021-2022). In this web-app, Exploratory Data Analysis (EDA) for three datasets is performed and both basic & interactive visualizations are also formed. These data sets are presented in the following tables and their decriptions are given in the report.**') 
    data=pd.read_csv(r'C:\Users\HP\streamlit_apps\multipage\city_temp.csv')
    st.success('1. City-Tempertature Dataset')
    AgGrid(data)
    data1=pd.read_csv(r'C:\Users\HP\streamlit_apps\multipage\westmidlands_crime.csv')
    data1=data1.drop('Crime ID', axis=1)
    st.success('2. West Midlands Crime Dataset')
    AgGrid(data1)
    data2=pd.read_csv(r'C:\Users\HP\streamlit_apps\multipage\melanoma-1.csv')
    st.success('2. Malignant Melanoma Dataset')
    AgGrid(data2)
    