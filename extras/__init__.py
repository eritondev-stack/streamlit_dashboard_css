import streamlit as st
import os

def padding(padding):
    return st.markdown(f"""
    <div style="height: {str(padding)}px; width: 2px;"></div>""", unsafe_allow_html=True)

def ancora(name):
    return st.markdown(f"<div class='{name}'></div>", unsafe_allow_html=True)
  
  
def loadCss():
    path = os.getcwd()
    f = open(path + "/css/index.css")
    css = f.read()
    f.close()   
    st.markdown(f"""
    <style>
    {css}
      </style>
      """, unsafe_allow_html=True)
