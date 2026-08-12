from logs.log import logger

"""
Autentifica o usuario
"""

from domain.jwt import JwtSession
from repository.manage import SessionJson


class AuthUser:

    def __init__(self)-> None:

        self.json = SessionJson()
        self.jwt = JwtSession()
        

    #valida se o token existe
    def exists(self) -> bool:

        return self.json.read() is not None

    #Cria o token e salva
    async def create(self, id:int, name:str) -> str:

        payload = {"id": id, "name":name}

        token = self.jwt.create(payload=payload)

        self.json.save(token=token)

        return await token

    #Le o json e le o token
    def read(self) -> None|dict:

        token = self.json.read()

        if token is None:
            return token

        payload = self.jwt.read(token_jwt=token)

        return payload


        

    


    

    
        
        

