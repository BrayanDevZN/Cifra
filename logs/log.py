"""
configuração global de logs
"""

import logging

# Configura o log para ir APENAS para o arquivo e limpa os handlers do terminal
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8',
    force=True  
)


#Variavel que carrega o log
logger = logging.getLogger(__name__)