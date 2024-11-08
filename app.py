import setup_paths
import streamlit as st

planilhao_page = st.Page("frontend/planilhao_page.py", title="PLANILHAO", icon=":material/favorite:",default=True)
estrategia_page = st.Page("frontend/estrategia_page.py", title="Estrategia")
grafico_page = st.Page("frontend/grafico_page.py", title="Grafico")

pg = st.navigation(
    {
       "Planilhao": [planilhao_page],
       "Estrategia": [estrategia_page],
       "Grafico": [grafico_page],
    }
)
pg.run()