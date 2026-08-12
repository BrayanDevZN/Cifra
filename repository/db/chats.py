from logs.log import logger


"""
mexe na tabela chat
"""

from sqlalchemy import text, Engine
from typing import Literal
class ChatsDbError(Exception):
    pass

class ConversationDb:

    def __init__(self, engine:Engine)-> None:

        self.eng = engine


    #Insere na tabela
    def insert(self, conversation_id:int, role:Literal["Ia", "User"], mensage:str) -> dict:

        try:

            logger.info(f"sanvando conversa...")

            with self.eng.begin() as session:

                result = session.execute(
                    text("insert into chats(conversation_id, role, mensage) values(:conversation_id, :role, :mensage) returning id"),
                    {"conversation_id": conversation_id, "role": role, "mensage": mensage}
                )

            return result.mappings().fetchone()

        except Exception as e:

            logger.error(e)
            raise ChatsDbError(e)

    #Seleciona o chat
    def select(self, conversation_id:int) -> dict:

        try:
        
                    logger.info(f"buscando conversa...")
        
                    with self.eng.begin() as session:
        
                        result = session.execute(
                            text("select * from chats where conversation_id = :conversation_id"),
                            {"conversation_id":conversation_id}
                        )
        
                    return result.mappings().fetchone()
        
        except Exception as e:
        
                    logger.error(e)
                    raise ChatsDbError(e)


    #Deleta chat
    def delete(self, id:int) -> None:

          try:
                   
                              logger.info(f"Deletando conversa...")
                   
                              with self.eng.begin() as session:
                   
                                   result = session.execute(
                                       text("delete from chats where id = :id"),
                                       {"id":id}
                                   )
                   
                                  
          except Exception as e:
                   
                               logger.error(e)
                               raise ChatsDbError(e)




        