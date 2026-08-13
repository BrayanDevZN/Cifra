"""
Agente que executa comandos no terminal
"""

from service.db.control_db import control_db
from infra.manage import ResponseOpenAI, Cor
from service.prompts.get import Prompts
from service.tools.cmd import cmd_tool

class CmdAgent:

    def __init__(self, conversation_id:int,prompt:str, response:ResponseOpenAI)->None:

        self.id = conversation_id
        self.prompt = prompt
        self.res = response
        self.system_prompt = Prompts().cmd["content"]
        

    #chama a llm
    def _response(self) -> None:

        self.response = self.res(msg=self.prompt, prompt=self.system_prompt).get()

    

    #Executa o comando no terminal
    def _cmd(self) -> None:

        view = Cor().ciano(f"Cifra: Executando comando '{self.response}'...")
        print(f"\033[s\r{view}", end="", flush=True)
        
        self.comand = cmd_tool(comand=self.response)

        print("\033[u\033[J", end="", flush=True)
        

    #Salva a ação
    def _save(self) -> None:

        control_db.actions.insert(conversation_id=self.id, action=self.comand)

    def run(self) -> str:

        self._response()
        self._cmd()
        self._save()

        return self.comand

    

   


    
        