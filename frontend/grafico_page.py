import streamlit as st
from backend.routers import botao_gerar_estrategia

st.title("Grafico Page")
data_ini = st.date_input("Selecione a Data Base:")
data_fim = st.date_input("Selecione a Data Base:")
if st.button("Gerar Estrategia"):
    df = botao_gerar_estrategia(data_base, ind_rentabilidade, ind_desconto, qtde_acoes)
    st.table(df)

