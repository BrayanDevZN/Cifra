from logs.log import logger


"""
mexe na tabela actions
"""

from sqlalchemy import text, Engine

class ActionsDbError(Exception):
    pass

class ConversationDb:

    def __init__(self, engine:Engine)-> None:

        self.eng = engine


    #Insere na tabela
    def insert(self, conversation_id:int, action:str) -> dict:

        try:

            logger.info(f"Salvando comando '{action}'...")

            with self.eng.begin() as session:

                result = session.execute(
                    text("insert into actions(conversation_id, action) values (:conversation_id, :action) returning id"),
                    {"conversation_id": conversation_id, "action":action}
                )

            return result.mappings().fetchone()

        except Exception as e:

            logger.error(e)
            raise ActionsDbError(e)

    #Seleciona todos so comandos executados
    def select(self, user_id:int) -> dict:

        try:
        
                    logger.info(f"buscando conversas...")
        
                    with self.eng.begin() as session:
        
                        result = session.execute(
                            text("select a.action from actions a inner join conversation c on c.id = a.conversation_id where c.user_id = :user_id"),
                            {"user_id":user_id}
                        )
        
                    return result.mappings().fetchone()
        
        except Exception as e:
        
                    logger.error(e)
                    raise ActionsDbError(e)
