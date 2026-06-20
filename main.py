import streamlit as st

st.set_page_config(
    page_title="Simulador Biobío – Grupo 5",
    page_icon="🔥",
    layout="wide"
)

pg = st.navigation([
    st.Page("simulador.py", title="Simulador", icon="🔥"),
    st.Page("contexto.py",  title="Contexto",  icon="📖"),
])

pg.run()
