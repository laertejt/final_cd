from backend.routers import menu_planilhao
import streamlit as st

st.title("PLANILHAO")
data_base = st.date_input("Digite a data base:")
df = menu_planilhao(data_base)
st.dataframe(df)