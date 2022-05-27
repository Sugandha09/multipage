import streamlit as st
import pandas as pd
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')
import plotly.express as px
import streamlit.components.v1 as components
from streamlit_folium import folium_static
import folium
import base64
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
import cufflinks
cufflinks.go_offline(connected=True)
init_notebook_mode(connected=True)
init_notebook_mode(connected=True)
import os

def app():
    st.subheader('Interactive Plots')
    data=pd.read_csv(r'C:\Users\HP\streamlit_apps\multipage\city_temp.csv')
    col1,col2,col3=st.columns([1,5,1])
    with col2:
        st.subheader("1. Interactive Multiple Line chart")
        st.write('The following multiple line plot shows Average temperatures of India, Egypt and China')
        d1=data.groupby(['Year', 'Country'])['AvgTemperature'].mean()
        line1 = hv.Curve(d1.loc[:, 'India'], label='India').opts(tools=['hover'])
        line2= hv.Curve(d1.loc[:, 'Egypt'], label='Egypt').opts(tools=['hover'])
        line3 = hv.Curve(d1.loc[:, 'China'], label='China').opts(tools=['hover'])
        mult_line_plot = line1 * line2 * line3
        mlp=mult_line_plot.opts(width=600, title='Avg Temperatures of India, Egypt and China', xlabel='Year', ylabel='Average Temp')
        mlp.opts(legend_position='right', show_grid=True)
        st.write(hv.render(mlp, backend='bokeh'))
        
        st.subheader('2. Interactive pie-chart')
        df=pd.read_csv(r'C:\Users\HP\streamlit_apps\multipage\westmidlands_crime.csv')
        d2=df['Town'].groupby([df['Month'],df['Town']]).count()
        df3=pd.DataFrame({'': d2.loc[:,'Birmingham'].index.tolist(), 'Birmingham':d2.loc[:,'Birmingham'].tolist(), 
                'Coventry': d2.loc[:,'Coventry'].tolist(), 'Sandwell':d2.loc[:,'Sandwell'].tolist(), 'Wolverhampton':
                d2.loc[:,'Wolverhampton'].tolist(),'Walsall': d2.loc[:,'Walsall'].tolist(), 'Dudley':
                 d2.loc[:,'Dudley'].tolist(), 'Solihull':d2.loc[:,'Solihull'].tolist()})
        df4=df3.set_index('').T
        df4['Total_Crime']= df4.iloc[:, 1:].sum(axis=1)
        df4.reset_index(inplace=True)
        fpc = px.pie(df4, values='Total_Crime', names='index', title='Total Criminal incidences in westmidlands over the given time period')
        st.plotly_chart(fpc)
        
        
        st.subheader('3. Interactive Histogram')
        df1= pd.read_csv(r'C:\Users\HP\streamlit_apps\multipage\melanoma-1.csv')
        fhg=df1[['thickness', 'age']].iplot(asFigure=True,
            kind='hist',
            histnorm='percent',
            barmode='overlay',
            xTitle='Age(years) & Thickness (mm)',
            yTitle='(%) of Articles',
            title='Distribution of Age and Thickness')
        st.plotly_chart(fhg)

    
    with col2:
        st.subheader('4. Interactive Scatter Plots')
    
        #df1=df1.astype({'status':'object'})
        #df1=df1.astype({'ulcer':'object'})
        #df1=df1.astype({'sex':'object'})
        df1['sex'] = df1['sex'].map({0: 'Females', 1: 'Males'})
        df1['status'] = df1['status'].map({1: 'Died', 2: 'Still Alive', 3:'Died-other'})
        df1['ulcer'] = df1['ulcer'].map({0: 'Abesent', 1: 'Present'})
        fsc=df1.iplot(asFigure=True,
            x='time',
            y='age',
            categories='sex',
            xTitle='Survival Time',
            yTitle='Age of Patients',
            title='Age vs Survival Time')
        st.plotly_chart(fsc)
    
        
        fsc1 = px.scatter(df1, x="time", y="thickness", marginal_x="histogram", marginal_y="histogram",color="sex", title='Scatter Plot with Marginal Distributions')
        st.plotly_chart(fsc1)
        
   
        fsc2= px.scatter(df1, x="age", y="time", color="sex", facet_col="status", title='Age vs Time with respect to Sex and Status' )
        st.plotly_chart(fsc2)
        
        
        
        
        st.subheader("5. Choropleth")
        data1 = data[['Country', 'Year', 'AvgTemperature']].groupby(['Country','Year']).mean().reset_index()
        cp=px.choropleth(data_frame=data1, locations="Country", locationmode='country names', animation_frame="Year",
                color='AvgTemperature', color_continuous_scale=["blue", "green", "red"],     
                title="Average Temperature of the given countries between 1995 and 2019",width=800, height=700)
        st.plotly_chart(cp)
        
    
        st.subheader("6. World Map")
        
        st.write('Clink the link below to see the map')
        st.write('https://mi-linux.wlv.ac.uk/~2048496/mappp.html')
         
    
        st.subheader("7. Animated Bar Chart")
        import bar_chart_race as bcr
        import ffmpeg
        import base64
        d1=data.groupby(['Year', 'Country'])['AvgTemperature'].mean()
        bar_data=pd.DataFrame({'Year': d1.loc[:,'India'].index.tolist(), 'Australia': d1.loc[:,'Australia'].tolist(), 'Egypt': d1.loc[:,'Egypt'].tolist()
                        ,'South Africa': d1.loc[:,'South Africa'].tolist(), 'China': d1.loc[:,'China'].tolist(),  'India': d1.loc[:,'India'].tolist(), 
                        'Japan': d1.loc[:,'Japan'].tolist(),  'United Kingdom': d1.loc[:,'United Kingdom'].tolist() })
        bar_data.set_index('Year', inplace=True)
        html_str= bcr.bar_chart_race(df=bar_data ,title='Variation in Average Temperature (Fahrenheit)', steps_per_period=1).data
     
        start = html_str.find('base64,')+len('base64,')
        end = html_str.find('">')

        video = base64.b64decode(html_str[start:end])
        st.video(video)
    
        
        st.subheader('8. 3D Map')
        mapp = open(r"C:\Users\HP\Downloads\cmap.html", 'r', encoding='utf-8')
        so = mapp.read() 
        print(so)
        components.html(so, height=500)
        
        st.subheader('9. 3D Map with hexagonal layer')
        mapp3 = open(r"C:\Users\HP\Downloads\hlm2.html", 'r', encoding='utf-8')
        so3 = mapp3.read() 
        print(so3)
        components.html(so3, height=500)
    
        st.subheader('10. 3D Map with column layer')
        mapp4 = open(r"C:\Users\HP\Downloads\newmap.html", 'r', encoding='utf-8')
        so4 = mapp4.read() 
        print(so4)
        components.html(so4, height=500)
    
    
        st.subheader('11. Bubble plot on a Map')
        mapp1 = open(r"C:\Users\HP\Downloads\coloredscatter.html", 'r', encoding='utf-8')
        so1 = mapp1.read() 
        print(so1)
        components.html(so1, height=500)
    
        st.subheader('12. Density Map')
        mapp2 = open(r"C:\Users\HP\Downloads\density.html", 'r', encoding='utf-8')
        so2 = mapp2.read() 
        print(so2)
        components.html(so2, height=500)
        
        
        