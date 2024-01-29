# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 23:38:31 2023

@author: DELL
"""

import streamlit as st
import base64
from PIL import Image

a='<p style="font-family:sans-serif; color:green; font-size: 25px;top:130px;text-align:center;">Block Diagram</p>'
st.markdown(a, unsafe_allow_html=True)
image = Image.open('C:/Users/DELL/Downloads/durga/pages/block.jpg')
st.image(image)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('C:/Users/DELL/OneDrive - Aditya Engineering College/Desktop/retina-pro/pages/m2.jpg') 