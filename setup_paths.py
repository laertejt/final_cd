import sys
from pathlib import Path

# Define o diretório base e o diretório backend
BASE_DIR = Path(__file__).parent
FRONT_DIR = BASE_DIR / 'frontend'
BACK_DIR = BASE_DIR / 'backend'

# Adiciona os diretórios ao sys.path
sys.path.append(str(BASE_DIR))
sys.path.append(str(FRONT_DIR))
sys.path.append(str(BACK_DIR))

# Configuração básica do logging
LOG_DIR = str(BACK_DIR) + '/logs'
import logging 
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=f'{LOG_DIR}/app.log',  # Nome do arquivo de log
                    filemode='a') 