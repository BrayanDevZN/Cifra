"""
Cria e le token jwt
"""

import jwt

class JwtSession:

    def __init__(self, sing:str)-> None:

        #Assinatura do token
        self.sing  = sing

        #Algoritimo que ira ser usado
        self.alg = "HS256"
        

    #Cria o token
    def create(self, payload:dict) -> str:

        token = jwt.encode(
            payload=payload,
            algorithm=self.alg,
            key=self.sing
        )

        return token


    #Le o token
    def read(self, token_jwt:str) -> dict:

        token = jwt.decode(
            algorithms=[self.alg],
            jwt=token_jwt,
            key=self.sing
        )

        return token