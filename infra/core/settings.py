"""
pega as variaveis de ambiente
"""

#Classe de erro
class EnvError(Exception):
    pass

try:

    from pathlib import Path
    import os
    from dotenv import load_dotenv

    #Caminho do env
    BASE_DIR = Path(__file__).resolve().parent

    #Carrega as variaveis de ambiente
    if os.path.exists(BASE_DIR / ".env"):
        load_dotenv(BASE_DIR / ".env")


    #Pega a url que faz conexão com banco de dados
    url = os.getenv(".env")

except Exception as e:

    raise EnvError(e)