# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:20:13 2023

@author: DELL

import streamlit as st
st.title("Main Page")
st.subheader('This is a subheader')
st.text_area('This is chinni')"""
import streamlit as st
import base64
from PIL import Image

m='<p style="font-family:sans-serif; color:red; font-size: 29px;text-align:center;">Contact Informaton</p>'
st.markdown(m, unsafe_allow_html=True)
col1, col2, col3,col4= st.columns(4,gap="small")

with col1:
   image = Image.open('C:/Users/DELL/Downloads/durga/pages/satya.jpeg')
   image1=image.resize((170,230))
   st.image(image1)
   a='<p style="font-family:sans-serif; color:green; font-size: 25px;text-align:center;">19MH1A0596</p>'
   st.markdown(a, unsafe_allow_html=True)
   a1='<p style="font-family:sans-serif; color:black; font-size: 18px;text-align:center;">O Satya Durga</p>'
   st.markdown(a1, unsafe_allow_html=True)
   a2='<p style="font-family:sans-serif; color:black; font-size: 18px;text-align:center;">Ph 7286950181</p>'
   st.markdown(a2, unsafe_allow_html=True)


with col2:
   image = Image.open('C:/Users/DELL/Downloads/durga/pages/gayatri.jpg')
   image1=image.resize((170,230))
   st.image(image1)
   b='<p style="font-family:sans-serif; color:green; font-size: 25px;text-align:center;">19MH1A05C0</p>'
   st.markdown(b, unsafe_allow_html=True)
   b1='<p style="font-family:sans-serif; color:black; font-size: 18px;text-align:center;">P Gayatri</p>'
   st.markdown(b1, unsafe_allow_html=True)
   b2='<p style="font-family:sans-serif; color:black; font-size: 18px;text-align:center;">Ph 9505123766</p>'
   st.markdown(b2, unsafe_allow_html=True)
   
   

with col3:
   image = Image.open('C:/Users/DELL/Downloads/durga/pages/teja.jpg')
   image1=image.resize((170,230))
   st.image(image1)
   m='<p style="font-family:sans-serif; color:green; font-size: 25px;text-align:center;">19MH1A0598</p>'
   st.markdown(m, unsafe_allow_html=True)
   m1='<p style="font-family:sans-serif; color:black; font-size: 18px;text-align:center;">P Surya Teja</p>'
   st.markdown(m1, unsafe_allow_html=True)
   m2='<p style="font-family:sans-serif; color:black; font-size: 18px;text-align:center;">Ph 7036884772</p>'
   st.markdown(m2, unsafe_allow_html=True)
with col4:
   image = Image.open('C:/Users/DELL/Downloads/durga/pages/narayana.jpg')
   image1=image.resize((170,230))
   st.image(image1)
   d='<p style="font-family:sans-serif; color:green; font-size: 25px;text-align:center;">19MH1A0572</p>'
   st.markdown(d, unsafe_allow_html=True)
   d1='<p style="font-family:sans-serif; color:black; font-size: 18px;text-align:center;">Ch Satyanarayana</p>'
   st.markdown(d1, unsafe_allow_html=True)
   d2='<p style="font-family:sans-serif; color:black; font-size: 18px;text-align:center;">Ph 8688258224</p>'
   st.markdown(d2, unsafe_allow_html=True)
   
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('C:/Users/DELL/Downloads/durga/pages/regi.jpg') 
