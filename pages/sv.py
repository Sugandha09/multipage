import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from io import BytesIO


def app():
    
    st.header('Static Visulaizations')
    data=pd.read_csv(r'C:\Users\HP\streamlit_apps\multipage\city_temp.csv')
    st.markdown('**This page will navigate though some static visualisations related with the datasets we have seen earlier**')
    col1,col2,col3=st.columns([5,1,5])
    with col1:
        st.subheader("1. Line charts")
        chart=st.selectbox('Select the chart type',['Simple Line Chart', 'Multiple Line Chart','Line Chart on a Grid with Customised Line-Style, Color and Width', 'Dual Y axis Line Chart'])
        if chart is None:
            st.stop()
        else:
            if chart == 'Simple Line Chart':
                st.subheader('Simple Line Chart')
                st.markdown('**Plotting the average annual tempratures of the selected Country from 1995 to 2019**')
                country=st.selectbox('Select a Country', data.Country.unique())
                d1=data.groupby(['Year', 'Country'])['AvgTemperature'].mean()
                fig= plt.figure()
                plt.plot(d1.loc[:, country].index, d1.loc[:, country])
                plt.xlabel('Years')
                plt.ylabel('Average Temprature')
                plt.title('Avg. Temp. of {} from 1995 to 2019'.format(country))
                plt.xticks(d1.loc[:, country].index, rotation=45);
                st.pyplot(fig)
                
            elif chart is 'Multiple Line Chart':
                st.subheader('Multiple Line Chart')
                st.markdown('**Comparing the average tempratures of two countries for specified years**')
                countries=st.multiselect('Select any two countries city', data.Country.unique())
                if len(countries)==2:
                    years=st.multiselect('Select five years for comparison', data.Year.unique())
                    if len(years)==5:
                        d=data.loc[(data["Country"].isin(countries)) & (data['Year'].isin(years))]
                        d1=d.groupby(['Year', 'Country'])['AvgTemperature'].mean()
                        fig= plt.figure()
                        plt.plot(years, d1.loc[:, countries[0]])
                        plt.plot(years, d1.loc[:, countries[1]])
                        plt.xlabel('Years')
                        plt.ylabel('Average Temprature')
                        plt.title('Comaprison of Avg. Temp. of {} and {}'.format(countries[0],countries[1]))
                        plt.legend(labels=[countries[0], countries[1]], loc=0)
                        plt.xticks(years, rotation=45);
                        st.pyplot(fig)
                    else:
                        st.write('Please select any two countries and five years in chronological order for comparison')
                    
     
            elif chart is 'Line Chart on a Grid with Customised Line-Style, Color and Width':
                st.subheader('Line Chart on a Grid, Customised Line-Style, Color and Width')
                st.markdown('**Plotting the average monthly temprature of a country for a whole specified year**')
                c=st.selectbox('Select any Country', data.Country.unique())
                y=st.selectbox('Select any year', data.Year.unique())
                linestyle=st.selectbox('Select the line style', ['--',':','-.','-'])
                col=st.selectbox('Select the line color', ['green','red','blue','cyan','magenta','yellow','black','white'])
                lw=st.selectbox('Select the line width', [1,2,3,4,5,6,7,8,9,10,11])
                d2=data.groupby(['Year','Month', 'Country'])['AvgTemperature'].mean()
                fig2=plt.figure()
                plt.style.use('seaborn-whitegrid')
                plt.plot(data['Month'].unique(), d2.loc[y,:, c], linestyle, color=col, linewidth=lw)
                plt.xlabel('Months')
                plt.ylabel('Average Temprature')
                plt.title('Average monthly Temprature of {} in {}'.format(c,y))
                plt.legend(labels=[c], loc=0)
                plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], rotation=45);
                st.pyplot(fig2)
    
            elif chart is 'Dual Y axis Line Chart':
                st.subheader('Dual Y axis Line Chart')
                st.markdown('**Plotting the average temperatures of two countries from 1995 to 2019**')
                co=st.multiselect('Select any two countries', data.Country.unique())
                if len(co)==2:
                    d3=data.groupby(['Year','Country'])['AvgTemperature'].mean()
                    fig3, ax1 = plt.subplots()
                    plt.grid(False)
                    ax2 = ax1.twinx()
                    ax1.plot(d3.loc[:,co[0]].index, d3.loc[:,co[0]], color='green')
                    ax2.plot(d3.loc[:,co[1]].index, d3.loc[:,co[1]], color='blue')
                    ax1.set_xlabel("Years")
                    ax1.set_ylabel("Average annual temperature of {}".format(co[0]), color='green')
                    ax1.set_xticks(d3.index.get_level_values('Year').unique())
                    fig3.autofmt_xdate(rotation=45)
                    ax1.tick_params(axis="y", labelcolor='green')
                    ax2.set_ylabel("Average annual temprature of {}".format(co[1]), color='blue')
                    ax2.tick_params(axis="y", labelcolor='blue')
                    fig3.suptitle("Average annual temperatures of {} & {} over the given years".format(co[0],co[1]))
                    st.pyplot(fig3)
                else:
                    st.write('Please select only two cities')
            
    with col3:
    
        st.subheader("2. Scatter Plot")
        chart1=st.selectbox('Select the chart type',['Basic Scatter Plot', 'Scatter Plot with Colored Points','Scatter Plot Using Different Markers', 'Simple 3D Scatter Plot'])
        if chart1 is None:
            st.stop()
        else:
            if chart1 is 'Basic Scatter Plot':
                st.subheader('Basic Scatter Plot')
                st.markdown('**Plotting the average temperature of two cities for a specified month of a specified year**')
                c=st.multiselect('Select two cities', data.City.unique())
                if len(c)!=2:
                    st.write('Please Select only two cities')
                
                else:
                    m=st.selectbox('Select a Month', data.Month.unique())
                    y=st.selectbox('Select a Year', data.Year.unique())
                    fig4, ax = plt.subplots()
                    plt.grid(False)
                    ax.scatter(data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==c[0])]['AvgTemperature'], data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==c[1])]['AvgTemperature'])
                    ax.set_xlabel('Average daily temprature of {}'.format(c[0]))
                    ax.set_ylabel('Average  daily temprature of {}'.format(c[1]))
                    ax.set_title('Average daily Tempratures of {} and {}'.format(c[0],c[1]))
                    st.pyplot(fig4)
    
            elif chart1 is 'Scatter Plot with Colored Points':
                st.subheader('Scatter Plot with colored points')
                st.markdown('**Plotting the average temperature of two cities for a specified month and year using Scatter plot with colored points**')
                co=st.multiselect('Select any two cities', data.City.unique())
                if len(co)!=2:
                    st.write('Please Select only two cities')
                
                else:
                    m=st.selectbox('Select a Month', data.Month.unique())
                    y=st.selectbox('Select a Year', data.Year.unique())
                    fig5, ax = plt.subplots()
                    plt.grid(False)
                    sp=ax.scatter(data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==co[0])]['AvgTemperature'], data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==co[1])]['AvgTemperature'], c=data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==co[1])]['AvgTemperature'], cmap='Spectral')
                    fig5.colorbar(sp)
                    ax.set_xlabel('{}'.format(co[0]))
                    ax.set_ylabel("{}".format(co[1]))
                    ax.set_title('Average tempratures of {} and {}'.format(co[0],co[1]))
                    st.pyplot(fig5)
            elif chart1 is 'Scatter Plot Using Different Markers':
                st.subheader('Scatter Plot using different markers')
                st.markdown('**Plotting the temperature of more than two countries using different markers**')
                c=st.multiselect('Select four cities', data.City.unique())
                if len(c)!=4:
                    st.write('Please Select four Cities')
                
                else:
                    m=st.selectbox('Select a Month', data.Month.unique())
                    y=st.selectbox('Select a Year', data.Year.unique())
                
                    fig6, ax = plt.subplots()
                    plt.grid(False)
                    ax.scatter(data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==c[0])]['AvgTemperature'], data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==c[1])]['AvgTemperature'], color='blue', marker= '*', label=c[1])
                    ax.scatter(data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==c[0])]['AvgTemperature'], data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==c[2])]['AvgTemperature'], color= 'red', marker='v', label=c[2])
                    ax.scatter(data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==c[0])]['AvgTemperature'], data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==c[3])]['AvgTemperature'], color= 'green', marker='.', label=c[3])
                    plt.legend(loc=0)
                    ax.set_xlabel('Average Temperatures of {}'.format(c[0]))
                    ax.set_ylabel("Average Temperatures of {} ,{} & {}".format(c[1], c[2], c[3]))
                    ax.set_title('Scatter plot using different markers')
                    st.pyplot(fig6)
                    
            elif chart1=='Simple 3D Scatter Plot':
                st.subheader('3D Scatter Plot')
                st.markdown('**Plotting a three dimensional scatter plot using temperatures of three different cities for a specified month and year**')
                c=st.multiselect('Select three cities', data.City.unique())
                if len(c)!=3:
                    st.write('Please Select three Cities')
                
                else:
                    m=st.selectbox('Select a Month', data.Month.unique())
                    y=st.selectbox('Select a Year', data.Year.unique())
                    plt.grid(False)
                    fig = plt.figure()
                    ax = plt.axes(projection ="3d")
                    ax.scatter3D(data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==c[0])]['AvgTemperature'], data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==c[1])]['AvgTemperature'], data.loc[(data['Month']==m) & (data['Year']==y) & (data['City']==c[2])]['AvgTemperature'], color = "green")
                    ax.set_xlabel('Average monthly temp of {}'.format(c[0]))
                    ax.set_ylabel('Average monthly temp of {}'.format(c[1]))
                    ax.set_zlabel('Average monthly temp of {}'.format(c[2]))
                    ax.set_title('3D Scatter Plot')
                    st.pyplot(fig)
    with col1:                
        st.subheader("3. Bar Charts")
        chart2=st.selectbox('Select the chart type',['Simple Vertical/ Horizontal Bar Chart', 'Colored Bar Chart with sorted Values', 'Grouped Bar Chart', 'Stacked Bar Chart','Percent Stacked Bar Chart']) 
        if chart2 is None:
            st.stop()
        else:
            if chart2 is 'Simple Vertical/ Horizontal Bar Chart':
                st.subheader('Simple Vertical/ Horizontal Bar Chart')
                st.markdown('**Plotting the temperature of different regions using Bar Chart**')
                d=data.groupby(['Region'])['AvgTemperature'].mean()
                bp=st.selectbox('Choose Horizontal or Vertical Bar Chart', ['Horizontal','Vertical'])
                if bp=='Vertical':
                    fig=plt.figure()
                    plt.bar(d.index, d);
                    plt.title('Simple Verical Bar Chart')
                    plt.xlabel('Region')
                    plt.ylabel('Average Temperature of Regions over the given time period')
                    plt.xticks(d.index, rotation=90)
                    st.pyplot(fig)
                elif bp=='Horizontal':
                    fig=plt.figure()
                    plt.barh(d.index, d);
                    plt.title('Simple Horizontal Bar Chart')
                    plt.ylabel('Region')
                    plt.xlabel('Average Temperature of Regions over the given time period')
                    st.pyplot(fig)
            elif chart2=='Colored Bar Chart with sorted Values':
                st.subheader('Colored Bar Chart with sorted Values')
                st.markdown('**Plotting the temperature of different regions using Colored Bar Chart and sorted bars**')
                s=st.selectbox('Choose sorting',['Ascending','Descending'])
                if s=='Ascending':
                    d=data.groupby(['Region'])['AvgTemperature'].mean().sort_values()
                    fig=plt.figure()
                    plt.barh(d.index, d, color=['pink','yellow','green','blue','red']);
                    plt.title('Simple Horizontal Bar Chart')
                    plt.ylabel('Region')
                    plt.xlabel('Average Temperature of Regions over the given time period')
                    plt.legend()
                    st.pyplot(fig)
                elif s=='Descending':
                    d=data.groupby(['Region'])['AvgTemperature'].mean().sort_values(ascending=False)
                    fig=plt.figure()
                    plt.barh(d.index, d, color=['red','blue','green','yellow','pink']);
                    plt.title('Simple Horizontal Bar Chart')
                    plt.ylabel('Region')
                    plt.xlabel('Average Temperature of Regions over the given time period')
                    plt.legend()
                    st.pyplot(fig)
            elif chart2== 'Grouped Bar Chart':
                st.subheader('Grouped Bar Chart')
                st.markdown('**Plotting the Average temperature of any two regions over the given years using Grouped Bar Chart**')
                d=data.groupby(['Region', 'Year'])['AvgTemperature'].mean()   
                r=st.multiselect('Select two regions', data.Region.unique())
                if len(r)!=2:
                    st.write('Please Select only 2 Regions')
                else:
                    labels = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
                            '2017', '2018', '2019']
                    bar1 = d.loc[r[0],:].values
                    bar2 = d.loc[r[1],:].values

                    x = np.arange(len(labels))  # the label locations
                    width = 0.35  # the width of the bars

                    fig, ax = plt.subplots()
                    rects1 = ax.bar(x - width/2, bar1, width, label=r[0])
                    rects2 = ax.bar(x + width/2, bar2, width, label=r[1])

                    # Add some text for labels, title and custom x-axis tick labels, etc.
                    ax.set_ylabel('Avg Temperature')
                    ax.set_title('Grouped Bar Chart')
                    ax.set_xticks(x)
                    ax.set_xticklabels(['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
                    '2017', '2018', '2019'], rotation=45)

                    ax.legend()

                    fig.tight_layout()

                    st.pyplot(fig)
                
            elif chart2== 'Stacked Bar Chart':
                st.subheader('Stacked Bar Chart')
                st.markdown('**Plotting the Average temperature of any two regions over the given years using Stacked Bar Chart**')
                d=data.groupby(['Region', 'Year'])['AvgTemperature'].mean()   
                r=st.multiselect('Select two regions', data.Region.unique())
                if len(r)!=2:
                    st.write('Please Select only 2 Regions')
                else:
                    labels = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
                            '2017', '2018', '2019']
                
                    bar1 = d.loc[r[0],:].values
                    bar2 = d.loc[r[1],:].values
                    width = 0.50       # the width of the bars: can also be len(x) sequence

                    fig, ax = plt.subplots()

                    ax.bar(labels, bar1, width, label=r[0])
                    ax.bar(labels, bar2, width, bottom=bar1,label=r[1])

                    ax.set_ylabel('Average Temperatures')
                    ax.set_xlabel('Years')
                    ax.set_title('Stacked Bar Chart')
                    ax.set_xticklabels(['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
                    '2017', '2018', '2019'], rotation=45)
                    ax.legend()

                    st.pyplot(fig)
                
            elif chart2== 'Percent Stacked Bar Chart':
                st.subheader('Percent Stacked Bar Chart')
                st.markdown('**Plotting the Average temperature of any three regions over the given years using Percent Stacked Bar Chart**')
                d=data.groupby(['Region','Year'])['AvgTemperature'].mean()
                a=data.Year.unique()
                b=d.loc['Africa',:].values
                c=d.loc['Asia',:].values
                e=d.loc['Europe',:].values
                f=d.loc['Middle East',:].values
                g=d.loc['Australia/South Pacific',:].values
                df=pd.DataFrame({'Years':a, 'Africa':b, 'Asia':c,'Europe':e,'Middle East': f,'Australia/South Pacific':g})
                r=st.multiselect('Select three regions', data.Region.unique())
                if len(r)!=3:
                    st.write('Please Select only 3 Regions')
                else:
                    m = list(range(1,26)) 
                    totals = [i+j+k for i,j,k in zip(df[r[0]], df[r[1]], df[r[2]])]
                    r[0] = [i / j * 100 for i,j in zip(df[r[0]], totals)]
                    r[1] = [i / j * 100 for i,j in zip(df[r[1]], totals)]
                    r[2] = [i / j * 100 for i,j in zip(df[r[2]], totals)]
                    barWidth = 0.85
                    names = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
                        '2017', '2018', '2019']
                    fig=plt.figure()
                    plt.bar(m, r[0], color='#b5ffb9', edgecolor='white', width=barWidth, label=r[0])
                    plt.bar(m, r[1], bottom=r[0], color='#f9bc86', edgecolor='white', width=barWidth, label=r[1])
                    plt.bar(m, r[2], bottom=[i+j for i,j in zip(r[0], r[1])], color='#a3acff', edgecolor='white', width=barWidth, label=r[2])
                    plt.xticks(m, names, rotation=45)
                    plt.xlabel("Years")
                    plt.title('Percent Stacked Bar Chart')
                    plt.legend()
                    st.pyplot(fig)
    
    data1=pd.read_csv(r'C:\Users\HP\streamlit_apps\multipage\westmidlands_crime.csv')
    with col3:
        st.subheader("4. Pie charts")
        chart3=st.selectbox('Select the chart type',['Basic Pie Chart with Shadow', 'Pie chart with pulled pies', 'Donut Chart', 'Nested Pie Chart'])
        if chart3 is None:
            st.stop()
        elif chart3=='Basic Pie Chart with Shadow':
            st.subheader('Basic Pie Chart with shadow')
            st.markdown('**This Pie Chart represents distribution of 6 most frequent crimes occured in areas of West Midlands from January 2021 to July 2021**')
            labels = data1 [ 'Crime type' ]. value_counts().nlargest(n=6).index
            m=data1 [ 'Crime type' ]. value_counts().nlargest(n=6).values
            n=sum(m)
            sizes = [ round((x*100)/n,1) for x in m]
            #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes,labels=labels, autopct='%1.1f%%', shadow= True, startangle=90)
            ax1.axis('equal')
            plt.title('Crime types and their likelihood in areas of West Midlands')
            st.pyplot(fig1)
    
        elif chart3=='Pie chart with pulled pies':
            st.subheader('Pie chart with pulled pies')
            st.markdown('**This Pie Chart represents distribution of 6 most frequent crimes occured in areas of West Midlands from January 2021 to July 2021**')
            labels = data1 [ 'Crime type' ]. value_counts().nlargest(n=6).index
            m=data1 [ 'Crime type' ]. value_counts().nlargest(n=6).values
            n=sum(m)
            sizes = [ round((x*100)/n,1) for x in m]
            explode = (0.05, 0.05, 0.05, 0.05,0.05,0.05)  # only "explode" the 2nd slice (i.e. 'Hogs')

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes,labels=labels,explode=explode, autopct='%1.1f%%',
            shadow=False, startangle=90)
            ax1.axis('equal')
            plt.title('Crime types and their likelihood in areas of West Midlands')
            st.pyplot(fig1)
    
        elif chart3=='Donut Chart':
            st.subheader('Donut Chart')
            st.markdown('**This Pie Chart represents distribution of 6 most frequent crimes occured in areas of West Midlands from January 2021 to July 2021**')
            labels = data1 [ 'Crime type' ]. value_counts().nlargest(n=6).index
            m=data1 [ 'Crime type' ]. value_counts().nlargest(n=6).values
            n=sum(m)
            sizes = [ round((x*100)/n,1) for x in m]
        
            colors = ['#FF0000', '#0000FF', '#FFFF00', '#ADFF2F', '#FFA500','deeppink']
            explode = (0.05, 0.05, 0.05, 0.05, 0.05,0.05)
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes,colors=colors, labels=labels,
            autopct='%1.1f%%', pctdistance=0.85,
            explode=explode)
  
            centre_circle = plt.Circle((0, 0), 0.70, fc='white')
            fig1 = plt.gcf()
  
            fig1.gca().add_artist(centre_circle)
  
            plt.title('Crime types and their likelihood in areas of West Midlands')
            st.pyplot(fig1)
  
        elif chart3=='Nested Pie Chart':
            st.subheader('Nested Pie Chart')
            st.markdown('**This Pie Chart represents distribution of 2 most frequent crimes occured in Birmingham, Wolverhampton and Dudley from January 2021 to July 2021**')
        
            d=data1.loc[data1['Town'].isin(['Birmingham','Wolverhampton', 'Dudley'])]
            d1=d.loc[d['Crime type'].isin(['Violence and sexual offences',
                               'Anti-social behaviour'])]
        
            size1= d1['Town'].value_counts().values
            size2= d1[ 'Town'] . groupby ([ d1[ 'Town' ], d1[ 'Crime type' ]]) . count ().values
            labels1=['Birmingham','Wolverhampton', 'Dudley']
            labels2=['Violence and sexual offences','Anti-social behaviour','Violence and sexual offences','Anti-social behaviour', 'Violence and sexual offences','Anti-social behaviour']

            a,b,c = [plt.cm.summer, plt.cm.autumn, plt.cm.winter ]

            outer_colors = [a(.6), b(.6),c(.6)]
            inner_colors = [a(.5), a(.4), 
                    b(.5),b(.4),c(.5),c(.4)]
            fig1, ax1 = plt.subplots()        
            size=0.3
            ax1.pie(size1, radius=1, colors=outer_colors,labels=labels1,
            wedgeprops=dict(width=size, edgecolor='w'))

            ax1.pie(size2, radius=1-size, colors=inner_colors,labels=labels2,
            wedgeprops=dict(width=size, edgecolor='w'))
        

            ax1.set(aspect="equal", title='Nested Donut Chart')
            st.pyplot(fig1)
    
    
    
    data2=pd.read_csv(r'C:\Users\HP\streamlit_apps\multipage\melanoma-1.csv')
    with col1:
        st.subheader("5. Histogram")
        chart4=st.selectbox('Select the chart type',['Basic Histogram', 'Histogram with mean and median line', '2D histogram or Density heat map'])
        if chart4 is None:
            st.stop()
        elif chart4=='Basic Histogram':
            st.subheader('Basic Histogram')
            st.markdown('Plotting three histograms together to show distribution of variables: thickness, age and time')
            n_bins=st.slider('please set the bin size', 5,50, 25)
            fig2, ax2 = plt.subplots(1,3, sharey=False, tight_layout = True)
            ax2[0].hist(data2['thickness'], bins=n_bins)
            ax2[1].hist(data2['age'], bins=n_bins)
            ax2[2].hist(data2['time'], bins=n_bins)
            ax2[0].set_xlabel('Thickness (mm)')
            ax2[1].set_xlabel('Age (years)')
            ax2[2].set_xlabel('Time (days survived')
            fig2.suptitle('Histograms presenting the distribution of Thickness, Age and Time')
            st.pyplot(fig2)
    
        elif chart4=='Histogram with mean and median line':
            st.subheader('Histogram with mean and median line')
            st.markdown('Plotting three histograms together to show distribution of variables: thickness, age and time with mean and median lines')
            n_bins=st.slider('please set the bin size', 5,50, 25)
            fig2, ax2 = plt.subplots(1,3, sharey=False, tight_layout = True)
            ax2[0].hist(data2['thickness'], bins=n_bins)
            ax2[1].hist(data2['age'], bins=n_bins)
            ax2[2].hist(data2['time'], bins=n_bins)
            ax2[0].set_xlabel('Thickness (mm)')
            ax2[1].set_xlabel('Age (years)')
            ax2[2].set_xlabel('Time (days survived')
            ax2[0].axvline(data2['thickness'].mean(), color='r', linestyle='dashed', linewidth=2, label='mean')
            ax2[0].axvline(data2['thickness'].median(), color='g', linestyle='dashed', linewidth=2, label='median')
            ax2[1].axvline(data2['age'].mean(), color='r', linestyle='dashed', linewidth=2, label='mean')
            ax2[1].axvline(data2['age'].median(), color='g', linestyle='dashed', linewidth=2, label='median')
            ax2[2].axvline(data2['time'].mean(), color='r', linestyle='dashed', linewidth=2, label='mean')
            ax2[2].axvline(data2['time'].median(), color='g', linestyle='dashed', linewidth=2, label='median')
            fig2.suptitle('Histograms presenting the distribution of Thickness, Age and Time')
            plt.legend()
            st.pyplot(fig2)
    
        elif chart4=='2D histogram or Density heat map':
            st.subheader('Histogram presenting the joint distribution of two variables')
            st.markdown('Plotting a density heat map or a 2D histogram to present the joint distribution of variables: time and age')
            fig2, ax2 = plt.subplots(tight_layout=True)
            h=ax2.hist2d(data2['time'], data2['age'])
            ax2.set_xlabel('Survival time in days')
            ax2.set_ylabel('Age in years')
            ax2.set_title('2D Histogram')
            fig2.colorbar(h[3], ax=ax2)
            st.pyplot(fig2)
    
    with col3:
        st.subheader("6. Boxplots")
        chart5=st.selectbox('Select the chart type',['Basic Boxplot', 'Notched Boxplot', 'Boxplot with different symbols showing outliers','Horizontal Boxplot', 'Multiple Boxplot'])
        if chart5 is None:
            st.stop()
        elif chart5=='Basic Boxplot':
            st.subheader('Basic Boxplot')
            st.markdown('Plotting a Boxplot to present the distribution of thickness, age and time')
            fig3, ax3 = plt.subplots(1,3, sharey=False, tight_layout = True)
            ax3[0].boxplot(data2['thickness'])
            ax3[1].boxplot(data2['age'])
            ax3[2].boxplot(data2['time'])
            ax3[0].set_xlabel('Thickness (mm)')
            ax3[1].set_xlabel('Age (years)')
            ax3[2].set_xlabel('Time (days survived')
            fig3.suptitle('Boxplots presenting the distribution of Thickness, Age and Time')
            st.pyplot(fig3)
    
        elif chart5=='Notched Boxplot':
            st.subheader('Notched Boxplot')
            st.markdown('Plotting a Notched Boxplot to present the distribution of thickness, age and time')
            fig3, ax3 = plt.subplots(1,3, sharey=False, tight_layout = True)
            ax3[0].boxplot(data2['thickness'],1)
            ax3[1].boxplot(data2['age'],1)
            ax3[2].boxplot(data2['time'],1)
            ax3[0].set_xlabel('Thickness (mm)')
            ax3[1].set_xlabel('Age (years)')
            ax3[2].set_xlabel('Time (days survived')
            fig3.suptitle('Boxplots presenting the distribution of Thickness, Age and Time')
            st.pyplot(fig3)  
    
        elif chart5=='Boxplot with different symbols showing outliers':
            st.subheader('Boxplot with different symbols showing outliers')
            st.markdown('Plotting a Boxplot with different symbols showing outliers to present the distribution of thickness, age and time')
            fig3, ax3 = plt.subplots(1,3, sharey=False, tight_layout = True)
            ax3[0].boxplot(data2['thickness'],0,'rD')
            ax3[1].boxplot(data2['age'],0,'rD')
            ax3[2].boxplot(data2['time'],0, 'rD')
            ax3[0].set_xlabel('Thickness (mm)')
            ax3[1].set_xlabel('Age (years)')
            ax3[2].set_xlabel('Time (days survived')
            fig3.suptitle('Boxplots presenting the distribution of Thickness, Age and Time')
            st.pyplot(fig3) 
      
        elif chart5=='Horizontal Boxplot':
            st.subheader('Horizontal Boxplot')
            st.markdown('Plotting Horizontal Boxplots to present the distribution of thickness, age and time')
            fig3, ax3 = plt.subplots(1,3, sharey=False, tight_layout = True)
            ax3[0].boxplot(data2['thickness'],0,'rD', 0)
            ax3[1].boxplot(data2['age'],0,'rD', 0)
            ax3[2].boxplot(data2['time'],0, 'rD', 0)
            ax3[0].set_xlabel('Thickness (mm)')
            ax3[1].set_xlabel('Age (years)')
            ax3[2].set_xlabel('Time (days survived')
            fig3.suptitle('Horizontal Boxplots presenting the distribution of Thickness, Age and Time')
            st.pyplot(fig3)
        
        elif chart5=='Multiple Boxplot':
            st.subheader('Multiple Boxplot')
            st.markdown('Boxplots presenting the distribution of Thickness of tumor for males and females')
            d0=data2.loc[data2['sex']==0]
            d1=data2.loc[data2['sex']==1]
            f=d0['thickness'].tolist()
            m=d1['thickness'].tolist()
            dict={'Females':f, 'Males': m}
            fig3, ax3 = plt.subplots()
            ax3.boxplot(dict.values(), 0 , 'rD')
            ax3.set_xticklabels(dict.keys());
            ax3.set_title('distribution of Thickness of tumor for males and females')
            st.pyplot(fig3)
    with col1:
        st.subheader("7. Bubble Plot")
        chart6=st.selectbox('Select the chart type',['Basic Bubble plot', 'Custom Bubble plot'])
        if chart6 is None:
            st.stop()
        elif chart6=='Basic Bubble plot':
            st.subheader('Basic Bubble Plot')
            st.markdown('Bubble plot presenting relationship of three variables: age, time and thickness')
            x= data2['time']
            y=data2['age']
            z=data2['thickness']
            fig4,ax4 =plt.subplots()
            ax4.scatter(x, y, s=z*100,alpha=0.5)
            ax4.set_xlabel('Survival days')
            ax4.set_ylabel('Age')
            ax4.set_title('Bubble plot presenting relationship of age, time and thickness')
            st.pyplot(fig4)
    
        elif chart6=='Custom Bubble plot':
            st.subheader('Bubble plot with different marker style and color')
            st.markdown('Bubble plot presenting relationship of three variables: age, time and thickness')
            j=st.selectbox('Select Color',['red','green','yellow','magenta','cyan','blue','black','brown'])
            k=st.selectbox('Select shape',['s','D','v','^','p','*','d','o'])
            x= data2['time']
            y=data2['age']
            z=data2['thickness']
            fig4,ax4 =plt.subplots()
            ax4.scatter(x, y, s=z*100,c=j, marker=k,alpha=0.5)
            ax4.set_xlabel('Survival days')
            ax4.set_ylabel('Age')
            ax4.set_title('Bubble plot presenting relationship of age, time and thickness')
            st.pyplot(fig4)
    
    with col3:
        st.subheader("8. World Cloud")
        from wordcloud import WordCloud
        st.set_option('deprecation.showPyplotGlobalUse', False)
        chart6=st.selectbox('Select the chart type',['Simple World Cloud', 'World Cloud with stopwords', 'Customised World Cloud with different background and word color'])
        if chart6 is None:
            st.stop()
        elif chart6=='Simple World Cloud':
            st.subheader('Simple World Cloud')
            st.markdown('Following figure is a world cloud made from a chunk taken from article: "**Altair: Interactive Statistical Visualizations for Python**"')
            fig5=plt.figure()
            text=('Altair is a declarative statistical visualization library for Python. Statistical visualizationis a constrained subset of data visualization focused on the creation of visualizations that are helpful in statistical modeling. The constrained model of statistical visualization is usually expressed in terms of a visualization grammar (Wilkinson, 2005) that specifies how input data is transformed and mapped to visual properties (position, color, size, etc.). Altair is based on the Vega-Lite visualization grammar (Satyanarayan, Moritz, Wongsuphasawat, & Heer, 2017), which allows a wide range of statistical visualizations to be expressed using a small number of grammar primitives. Vega-Lite implements a view composition algebra in conjunction with a novel grammar of interactions that allow users to specify interactive charts in a few lines of code. Vega-Lite is declarative; visualizations are specified using JSON data that follows the Vega-Lite JSON schema')
            wordcloud = WordCloud(width=480, height=480, colormap="Blues").generate(text)
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            st.pyplot(fig5)
        
        elif chart6=='World Cloud with stopwords':
            st.subheader('World Cloud with stopwords')
            st.markdown('Following figure is a world cloud made from a chunk taken from article: "**Altair: Interactive Statistical Visualizations for Python**"')
        
            fig5=plt.figure()
            text=('Altair is a declarative statistical visualization library for Python. Statistical visualizationis a constrained subset of data visualization focused on the creation of visualizations that are helpful in statistical modeling. The constrained model of statistical visualization is usually expressed in terms of a visualization grammar (Wilkinson, 2005) that specifies how input data is transformed and mapped to visual properties (position, color, size, etc.). Altair is based on the Vega-Lite visualization grammar (Satyanarayan, Moritz, Wongsuphasawat, & Heer, 2017), which allows a wide range of statistical visualizations to be expressed using a small number of grammar primitives. Vega-Lite implements a view composition algebra in conjunction with a novel grammar of interactions that allow users to specify interactive charts in a few lines of code. Vega-Lite is declarative; visualizations are specified using JSON data that follows the Vega-Lite JSON schema')
            s=st.selectbox('Choose a word that you want to stop',['visualization','grammar','allow','JSON','of', 'is','to'])
            wordcloud = WordCloud(width=480, height=480,stopwords=s, colormap="Blues").generate(text)
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            st.pyplot(fig5)
    
        elif chart6=='Customised World Cloud with different background and word color':
            st.subheader('Customised World Cloud with different background and word color')
            st.markdown('Following figure is a world cloud made from a chunk taken from article: "**Altair: Interactive Statistical Visualizations for Python**"')
        
            fig5=plt.figure()
            text=('Altair is a declarative statistical visualization library for Python. Statistical visualizationis a constrained subset of data visualization focused on the creation of visualizations that are helpful in statistical modeling. The constrained model of statistical visualization is usually expressed in terms of a visualization grammar (Wilkinson, 2005) that specifies how input data is transformed and mapped to visual properties (position, color, size, etc.). Altair is based on the Vega-Lite visualization grammar (Satyanarayan, Moritz, Wongsuphasawat, & Heer, 2017), which allows a wide range of statistical visualizations to be expressed using a small number of grammar primitives. Vega-Lite implements a view composition algebra in conjunction with a novel grammar of interactions that allow users to specify interactive charts in a few lines of code. Vega-Lite is declarative; visualizations are specified using JSON data that follows the Vega-Lite JSON schema')
            s=st.selectbox('Choose background color',['skyblue','pink','yellow','darkgreen','white','Brown','Purple','Red','Black','Gold','Orange','Magenta'])
            t=st.selectbox('Choose word color',['Greys','Purples','Blues','Greens','Oranges','Reds','viridis', 'plasma', 'inferno', 'magma', 'cividis','YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu','GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'])
            wordcloud = WordCloud(width=480, height=480,colormap=t, background_color=s).generate(text)
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            st.pyplot(fig5)
    
    
        
    