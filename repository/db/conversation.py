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
    def insert(self, user_id:int, name:str, permission:Literal["total", "partial", "none"]) -> dict:

        try:

            logger.info(f"Criando chat {name}...")

            with self.eng.begin() as session:

                result = session.execute(
                    text("insert into conversation(user_id, name, permission) values (:user_id, :name, :permission) returning id, name"),
                    {"user_id":user_id,"name":name, "permission":permission}
                )

            return result.mappings().fetchone()

        except Exception as e:

            logger.error(e)
            raise ConversationDbError(e)

    #Seleciona o chat
    def select(self, user_id:int) -> dict:

        try:
        
                    logger.info(f"buscando conversas...")
        
                    with self.eng.begin() as session:
        
                        result = session.execute(
                            text("select * from conversation where user_id = :user_id"),
                            {"user_id":user_id}
                        )
        
                    return result.mappings().fetchone()
        
        except Exception as e:
        
                    logger.error(e)
                    raise ConversationDbError(e)

    #Atualiza nome
    def update(self, Set:Literal["name", "permission"], id:int, value:str) -> dict:

         try:
         
                    logger.info(f"Atualizando {Set} para {value}...")

                    
         
                    with self.eng.begin() as session:
         
                         result = session.execute(
                             text("update conversation set :Set = :value where id = :id"),
                             
                                {"Set": Set, "value":value, "id":id}
                                                          
                         )
         
                    return result.mappings().fetchone()
         
         except Exception as e:
         
                     logger.error(e)
                     raise ConversationDbError(e)

    #Deleta chat
    def delete(self, id:int) -> None:

          try:
                   
                              logger.info(f"Deletando chat...")
                   
                              with self.eng.begin() as session:
                   
                                   result = session.execute(
                                       text("delete from conversation where id = :id"),
                                       {"id":id}
                                   )
                   
                                  
          except Exception as e:
                   
                               logger.error(e)
                               raise ConversationDbError(e)




        