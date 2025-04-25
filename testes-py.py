import streamlit as st
import os

# Obtenha o diretório atual deste arquivo
base_dir = os.path.expandvars("$HOME/site/wwwroot")

st.write("Imagem 1")
st.image("assets/sliter.jpg", use_container_width=True)

st.write("Imagem 2")
logo_path = os.path.join(base_dir, "assets", "sliter.jpg")
st.image(logo_path, use_container_width=True)
