"""
Le todos os prompts e salva em suas variaveis
"""

try:
    from repository.manage import read
    from infra.manage import CMD, MANAGER, SECURITY

    CMD["content"] = read(CMD)
    MANAGER["content"] = read(MANAGER)
    SECURITY["content"] = read(SECURITY)


    #Classe que vai carregar os prompt para outras partes do codigo

    class Prompts:

        cmd = CMD
        manager = MANAGER
        security = SECURITY

except Exception as e:

    raise Exception(e)


    


