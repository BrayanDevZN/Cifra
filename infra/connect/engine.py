from logs.log import logger

"""
cria conexão com banco de dados
"""

class CreateEngineError(Exception):
    pass


from sqlalchemy import create_engine, Engine

def engine(url:str) -> Engine:

    try:

        logger.info("Criando conexão com banco de dados...")

        return create_engine(url)

    except Exception as e:
        raise CreateEngineError(e)


