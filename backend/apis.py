import os
import requests
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("TOKEN")
headers = {"Authorization": "JWT {}".format(token)}
import logging
logger = logging.getLogger(__name__)

def pegar_planilhao(data_base):
    """
    Consulta todas as ações com os principais indicadores fundamentalistas

    params:
    data_base (date): Data Base para o cálculo dos indicadores.

    return:
    dados (list): lista com o dicionario com todas as Ações.
    """
    params = {'data_base': data_base}
    try:
        r = requests.get('https://laboratoriodefinancas.com/api/v1/planilhao',params=params, headers=headers)
        if r.status_code == 200:
            dados = r.json()
            logger.info(f"Dados do Planilhao consultados com sucesso: {data_base}")
            print(f"Dados do Planilhao consultados com sucesso: {data_base}")
            return dados
        else:
            logger.error(f"Erro na consulta do planilhao: {data_base}")
            print(f"Erro na consulta do planilhao: {data_base}")
    except Exception as e:
        logger.error(f"ERRO TECNICO: {e}")
        print(f"ERRO TECNICO: {e}")


def get_preco_corrigido(data_ini, data_fim, ticker):

    params = {
            'ticker': ticker,
            'data_ini': data_ini,
            'data_fim': data_fim
            }
    try:
        r = requests.get('https://laboratoriodefinancas.com/api/v1/preco-corrigido',params=params, headers=headers)
        if r.status_code == 200:
            dados = r.json()
            logger.info(f"Dados do Preco Corrigido consultados com sucesso: {ticker}")
            print(f"Dados do Preco Corrigido consultados com sucesso: {ticker}")
            return dados
        else:
            logger.error(f"Erro na consulta do Preco Corrigido: {ticker}")
            print(f"Erro na consulta do Preco Corrigido: {ticker}")
    except Exception as e:
        logger.error(f"ERRO TECNICO: {e}")
        print(f"ERRO TECNICO: {e}")

def get_preco_diversos(data_ini, data_fim, ticker):

    params = {
            'ticker': ticker,
            'data_ini': data_ini,
            'data_fim': data_fim
            }
    try:
        r = requests.get('https://laboratoriodefinancas.com/api/v1/preco-diversos',params=params, headers=headers)
        if r.status_code == 200:
            dados = r.json()
            logger.info(f"Dados do Preco diversos consultados com sucesso: {ticker}")
            print(f"Dados do Preco diversos consultados com sucesso: {ticker}")
            return dados
        else:
            logger.error(f"Erro na consulta do Preco diversos: {ticker}")
            print(f"Erro na consulta do Preco diversos: {ticker}")
    except Exception as e:
        logger.error(f"ERRO TECNICO: {e}")
        print(f"ERRO TECNICO: {e}")