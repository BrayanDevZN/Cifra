from logs.log import logger

"""
le e salva o arquivo json em infra/core/sessio.json onde vai ser armazenado o token do usuario
"""

import json
import os
class SessionJson:

    def __init__(self)-> None:

        self.path = "infra/core/session.json"

    #Salva o json
    def save(self, token:str) -> None:

        try:

            logger.info(f"Salvando token...")

            with open(self.path, "w", encoding="utf-8") as f:

                json.dump({"token": token}, f, ensure_ascii=False)

        except Exception as e:
            raise Exception(e)

    #Le
    def read(self) -> str|None:

        try:

            logger.info("Procurando token...")

            if not os.path.exists(self.path) :

                logger.info("Token não encontrado!!")

                return None

            with open(self.path, "r") as f:

                data = json.load(f)

            return data["token"]

        except Exception as e:

            raise Exception(e)



        

