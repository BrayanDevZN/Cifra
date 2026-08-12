from logs.log import logger


"""
mexe na tabela conversation
"""

from sqlalchemy import text, Engine
from typing import Literal
class ConversationDbError(Exception):
    pass

class ConversationDb:

    def __init__(self, engine:Engine)-> None:

        self.eng = engine


    #Insere na tabela
    def insert(self, user_id:int, name:str) -> dict:

        try:

            logger.info(f"Criando chat {name}...")

            with self.eng.begin() as session:

                result = session.execute(
                    text("insert into conversation(user_id, name) values (:user_id, :name) returning id, name"),
                    {"user_id":user_id,"name":name}
                )

            return result.mappings().fetchone()

        except Exception as e:

            logger.error(e)
            raise ConversationDbError(e)

    #Seleciona o chat
    def select(self, id:int) -> dict:

        try:
        
                    logger.info(f"buscando conversas...")
        
                    with self.eng.begin() as session:
        
                        result = session.execute(
                            text("select * from conversation where id = :id"),
                            {"id":id}
                        )
        
                    return result.mappings().fetchone()
        
        except Exception as e:
        
                    logger.error(e)
                    raise ConversationDbError(e)

    #Atualiza nome
    def update(self, name:str, id:int) -> dict:

         try:
         
                    logger.info(f"Atualizando chat para {name}...")
         
                    with self.eng.begin() as session:
         
                         result = session.execute(
                             text("update conversation set name = :name where id = :id"),
                             {"name":name,  "id":id}
                         )
         
                    return result.mappings().fetchone()
         
         except Exception as e:
         
                     logger.error(e)
                     raise ConversationDbError(e)

    #Deleta usuario
    def delete(self, id:int) -> None:

          try:
                   
                              logger.info(f"Deletando usuario...")
                   
                              with self.eng.begin() as session:
                   
                                   result = session.execute(
                                       text("delete from conversation where id = :id"),
                                       {"id":id}
                                   )
                   
                                  
          except Exception as e:
                   
                               logger.error(e)
                               raise ConversationDbError(e)




        