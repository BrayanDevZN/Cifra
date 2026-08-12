from logs.log import logger


"""
mexe na tabela users
"""

from sqlalchemy import text, Engine
from typing import Literal
class UsersDbError(Exception):
    pass

class UsersDb:

    def __init__(self, engine:Engine)-> None:

        self.eng = engine


    #Insere na tabela
    def insert(self, name:str, email:str, password:str) -> dict:

        try:

            logger.info(f"Criando usuario {name}...")

            with self.eng.begin() as session:

                result = session.execute(
                    text("insert into users(name, email, password) values (:name, :email, :password) returning id, name"),
                    {"name":name, "email": email, "password":password}
                )

            return result.mappings().fetchone()

        except Exception as e:

            logger.error(e)
            raise UsersDbError(e)

    #Seleciona usuario
    def select(self, id:int) -> dict:

        try:
        
                    logger.info(f"buscando usuario...")
        
                    with self.eng.begin() as session:
        
                        result = session.execute(
                            text("select * from users where id = :id"),
                            {"id":id}
                        )
        
                    return result.mappings().fetchone()
        
        except Exception as e:
        
                    logger.error(e)
                    raise UsersDbError(e)

    #Atualiza senha ou nome
    def update(self, Set:Literal["name"], value:str, id:int) -> dict:

         try:
         
                    logger.info(f"Atualizando usuario...")
         
                    with self.eng.begin() as session:
         
                         result = session.execute(
                             text("update users set :set = :value where id = :id"),
                             {"set":Set, "value":value, "id":id}
                         )
         
                    return result.mappings().fetchone()
         
         except Exception as e:
         
                     logger.error(e)
                     raise UsersDbError(e)

    #Deleta usuario
    def delete(self, id:int) -> None:

          try:
                   
                              logger.info(f"Deletando usuario...")
                   
                              with self.eng.begin() as session:
                   
                                   result = session.execute(
                                       text("delete from users where id = :id"),
                                       {"id":id}
                                   )
                   
                                  
          except Exception as e:
                   
                               logger.error(e)
                               raise UsersDbError(e)




        
        