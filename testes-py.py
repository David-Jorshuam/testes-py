import streamlit as st
import base64
import os

# Obtenha o diretório atual deste arquivo
base_dir = os.getcwd()

# Função para renderizar o conteúdo SVG
def render_svg(svg_path, width=None):
    svg_path = os.path.join(base_dir, svg_path)
    with open(svg_path, "r", encoding="utf-8") as file:
        svg_content = file.read()
        b64 = base64.b64encode(svg_content.encode("utf-8")).decode("utf-8")
        img_tag = f'<img src="data:image/svg+xml;base64,{b64}"'
        if width:
            img_tag += f' width="{width}"'
        img_tag += '>'
        return img_tag

# Criar uma coluna para alinhar as logos no meio
col1, col2, col3 = st.columns([1, 4, 1])  # Aumentando a coluna central (col2) para centralizar

with col1:
    st.empty()  # Deixa o espaço vazio à esquerda

with col2:
    # Adiciona as três logos de forma centralizada
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
            <div>{render_svg('assets/logo_unifor.svg', width=150)}</div>
            <div>{render_svg('assets/Logo_esm.svg', width=150)}</div>
            <div>{render_svg('assets/logo_GEQ.svg', width=150)}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.empty()  # Deixa o espaço vazio à direita