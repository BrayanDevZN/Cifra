"""
junta todos os modulos
"""

#Cria a engine
from infra.core.settings import url, key
from infra.connect.engine import engine

enginedb = engine(url=url)


#Inicializa o banco de dados
from infra.connect.init import InitDb

init = InitDb(engine=enginedb)
init.run()

#Junta a chave a api com a open ai
from infra.request.openai import Response

class ResponseOpenAI:

    def __init__(self, msg:str, prompt:str)-> None:

        self.instance = Response(key=key, mensage=msg, prompt=prompt)

    def get(self) -> None:

        return self.instance.get()


#Pega a configuração de cor
from infra.core.color import Cor


#Configurações de prompt
from infra.core.skills import SECURITY, CMD, MANAGER
    

    

    

        