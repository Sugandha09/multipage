import streamlit as st
import sweetviz as sv
import pandas as pd

def app():
    st.header('Exploratory Data Analysis')
    data=pd.read_csv(r'C:\Users\HP\streamlit_apps\multipage\city_temp.csv')
    data['Month']=data['Month'].astype('category')
    data['Year']=data['Year'].astype('category')
    data['Day']=data['Day'].astype('category')
    data['City']=data['City'].astype('category')
    advert_report = sv.analyze(data)
    #display the report
    advert_report.show_html('edatemp.html')
    
    data1=pd.read_csv(r'C:\Users\HP\streamlit_apps\multipage\westmidlands_crime.csv')
    data1=data1.drop('Crime ID', axis=1)
    data1=data1.drop('Context', axis=1)
    advert_report1 = sv.analyze(data1)
    #display the report
    advert_report1.show_html('edacrime.html')
    
    data2=pd.read_csv(r'C:\Users\HP\streamlit_apps\multipage\melanoma-1.csv')
    data2['year']=data2['year'].astype('category')
    advert_report2 = sv.analyze(data2)
    #display the report
    advert_report2.show_html('edamelanoma.html')
    