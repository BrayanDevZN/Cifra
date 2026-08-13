from logs.log import logger

"""
le os prompts
"""

import os

class NotFoundSkillError(str):
    pass

def read(config:dict) -> str:

    try:

        logger.info(f"Lendo skill {config["name"]}...")

        if not os.path.exists(config["path"]):
            raise NotFoundSkillError(f"Not found skill in path {config["path"]}")


        with open(config["path"], "r") as f:

            result = f.read()

        return str(result)

    except Exception as e:
        logger.error(e)
        raise Exception (e)



