"""
agente que verifica a permissão
"""

from infra.manage import ResponseOpenAI, Cor
from service.prompts.get import Prompts


class AgentSecurity:

    def __init__(self, response: ResponseOpenAI, comand:str, permission:str)->None:

        self.res = response
        self.comand = comand
        self.permission = permission
        self.system_prompt = Prompts().security["content"]


    def _response(self) -> None:

        self.response = self.res(msg=self.comand, prompt=self.system_prompt).get().get()

    #Verifica a permissão
    def _permission(self) -> None:

        view = Cor().ciano(f"Cifra: Verificando permissão para executar o  comando '{self.comand}'...")
        print(f"\r{view}", end="")

        match self.permission:

            case "total":

                self.status = True

            case "partial":

                self.status = self.response == "True"

            case "none":

                self.status = False


    #chama os metodos e retoorna o status
    def run(self) -> bool:

        self._permission()
        return self.status


        