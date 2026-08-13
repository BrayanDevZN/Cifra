from logs.log import logger

"""
Cria arquivo e le
"""

import os


class CodeToolError(Exception):
    pass

class CodeTool:



    #Salva  o codigo
    @staticmethod
    def save(file_name: str, content:str) -> None:

        try:

            logger.info(f"Criando arquivo {file_name}...")

            with open(file_name, "w", encoding="utf-8") as f:

                f.write(content)

        except Exception as e:

            logger.error(e)

            raise CodeToolError(e)


    #Le o codigo
    @staticmethod
    def read(file_name: str) -> str|None:

        try:
            logger.info(f"Lendo {file_name}...")

            if not os.path.exists(file_name):
                logger.warning(f"{file_name} não existe!!")

                return None

            with open(file_name, "r") as f:

                file = f.read(file_name)

            return file

        except Exception as e:

            logger.error(e)
            raise CodeToolError(e)

            



        