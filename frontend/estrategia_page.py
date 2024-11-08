import streamlit as st
from backend.routers import botao_gerar_estrategia

st.title("Estrategia Page")
ind_rentabilidade = st.radio("Selecione", ["roe", "roc", "roic"])
ind_desconto = st.radio("Selecione", ["earning_yield", "dividend_yield", "p_vp"])
data_base = st.date_input("Selecione a Data Base:")
qtde_acoes = st.text_input("Digite o numero de acoes da carteira:")
 
if st.button("Gerar Estrategia"):
    df = botao_gerar_estrategia(data_base, ind_rentabilidade, ind_desconto, int(qtde_acoes))
    st.table(df)

