# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 21:48:36 2023

@author: DELL
"""
import streamlit as st
import base64
m='<p style="font-family:sans-serif; color:red; font-size: 29px;text-align:center;">ABSTRACT</p>'
st.markdown(m, unsafe_allow_html=True)
a = '<p style="font-family:sans-serif; color:Green; font-size: 19px;margin-left:10px">Pupillometric Device for Detecting the Inherited Retinal Diseases in a Pediatric Age</p>'
st.markdown(a, unsafe_allow_html=True)
b='<p style="font-family:sans-serif;color:black;font-size:17px;">Inherited retinal diseases cause severe visual defects in children are classified into inner and outer retina diseases, and frequently cause visual deficiency in children. The analysis for this kind of disease is challenging, given the wide range of clinical and hereditary causes (with more than 200 causative qualities).It is regularly founded on an intricate example of complex pattern of clinical tests, including invasive ones, not always good for infants or young children. A different approach is needed, that exploits Pupillometry, a technique increasingly used to assess outer and inner retina functions and including gather the diameter of the pupil. A Clinical Decision Support System,in the view of Machine Learning utilizing Pupillometry to help the determination of Inherited retinal sicknesses in pediatric age.A Stacking Ensemble classifier (Support Vector Machine algorithm, Logistic Regression and Decission Tree) is used for prediction of Inherited Retinal Diseases.</p>'
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
add_bg_from_local('C:/Users/DELL/OneDrive - Aditya Engineering College/Desktop/retina-pro/pages/bg.jpg') 

