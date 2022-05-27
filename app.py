import streamlit as st

st.set_page_config(layout="wide")
from annotated_text import annotated_text
from PIL import Image


# Custom imports 
from multipage import MultiPage
from pages import introduction,sv,eda,iv# import your pages here

# Create an instance of the app 
app = MultiPage()

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# Title of the main page
st.title('Data Visualization using Python Libraries')

image = Image.open('C:\\Users\\HP\\streamlit_apps\\multipage\\landscape-colors.png')
st.image(image, caption='Overview of Data Visualization Libraries of Python (https://pyviz.org)')

# Add all your applications (pages) here
app.add_page("Datasets", introduction.app)
app.add_page("Exploratory Data Analysis", eda.app)
app.add_page("Static Visualizations", sv.app)
app.add_page("Interactive Visulaizations", iv.app)

# The main app
app.run()