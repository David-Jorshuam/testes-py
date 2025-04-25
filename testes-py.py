import streamlit as st
import os

# Obtenha o diretório atual deste arquivo
base_dir = os.path.expandvars("$HOME/site/wwwroot")

st.write("Imagem 1")
st.image("assets/sliter.jpg", width=150)

st.write("Imagem 2")
st.image("assets/logo_unifor.svg", width=150)

st.write("Imagem 3")
st.image("assets/logo_esm.svg", width=150)

st.write("Imagem 4")
st.image("assets/logo_GEQ.svg", width=150)
