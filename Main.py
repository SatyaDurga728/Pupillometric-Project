# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 18:48:53 2023

with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Projects", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
            
@author: DELL
"""
import streamlit as st
import base64
st.set_page_config(
        page_title="Home",
        page_icon="fa-buffer",
        layout="wide",
    )

a='<p style="font-family:sans-serif; color:pink; font-size: 28px;margin-top:130px;margin-right:200px;text-align:center;">Pupillometric Device for Detecting the Inherited Retinal Diseases in a Pediatric Age</p>'
st.markdown(a, unsafe_allow_html=True)
b='<p style="font-family:cursive; color:yellow; font-size: 20px;margin-top:10px;margin-left:10px;text-align:center;">- Your Eyes Our Vision</p>'
st.markdown(b, unsafe_allow_html=True)
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
add_bg_from_local('C:/Users/DELL/Downloads/durga/hero-bg.png')   
