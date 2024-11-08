import streamlit as st
from backend.views import gerar_grafico


st.title("Grafico Page")
data_ini = st.date_input("Selecione a Data Inicio:")
data_fim = st.date_input("Selecione a Data Fim:")
df = gerar_grafico()
# if st.button("Gerar Estrategia"):
#     df = botao_gerar_estrategia(data_base, ind_rentabilidade, ind_desconto, qtde_acoes)
#     st.table(df)

