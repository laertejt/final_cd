import streamlit as st
from backend.views import pegar_df_planilhao, gerar_estrategia


def menu_planilhao(data_base):
    df = pegar_df_planilhao(data_base)
    return df

def botao_gerar_estrategia(data_base, ind_rentabilidade, ind_desconto, qtde_acoes):
    df = gerar_estrategia(data_base, ind_rentabilidade, ind_desconto, qtde_acoes)
    return df