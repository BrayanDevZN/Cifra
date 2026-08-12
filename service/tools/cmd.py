from logs.log import logger

"""
tool que executa comando no terminal
"""

import subprocess

class CmdToolError(Exception):
    pass

def cmd_tool(comand:str) -> str|None:

    try:

        logger.info(f"Executando comando: {comand}...")

        result = subprocess.run(
            comand,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout.strip()

    except Exception as e:
        logger.error(e)
        raise CmdToolError(e)

