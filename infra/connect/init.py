from logs.log import logger


"""
cria as tabelas do banco que faltam
"""
class InitDbError(Exception):
    pass


from sqlalchemy import text, Engine, inspect

class InitDb:

    def __init__(self, engine:Engine) -> None:

        #Engine do banco
        self.eng = engine


        #Inspetor do banco
        self.inspector = inspect(engine)

        #Tabelas do banco
        self.tables = ["conversation", "actions", "chats"]


    #Deixa só as tabelas que ainda n existem em self.table
    def _exists(self) -> None:

        tables = [table for table in self.tables if not table in self.inspector.get_table_names()]

        self.tables = tables

        if self.table:
            logger.info(f"Criando {" ,".join(self.tables)}...")


    #Pega os comandos sql de cada tabela
    def _sql(self) -> None:

        try:

            sql = {"conversation": """
                            create table if not exists conversation(
                            id serial primary key,
                            name text not null
                            created_at timestamp default current_timestamp
                            )
                        """,
                        "actions": """
                                create table if not exists actions(
                                id serial primary key,
                                conversation_id int references conversation(id),
                                action text not null,
                                created_at timestamp default not null
                                )

                            """,
                        "chats":"""
                                    create table if not exists chats(
                                    id serial primary key,
                                    conversation_id int references conversation(id),
                                    role text not null,
                                    mensage text not null,
                                    created_at timestamp default current_timestamp
                                    )
                                """
                        }

            self.query = {query: sql[query] for query in self.tables}



        except Exception as e:
            raise InitDbError(e)

    #Executa as querys
    def _query(self) -> None:

        try:


            with self.eng.begin() as session:

                for  sql in self.query.values():

                    session.execute(
                        text(sql)
                    )


            logger.info(f"tabela(s) {" ,".join(self.tables)} !!!")

        except Exception as e:

            raise InitDbError(e)

    #Executa todos os metodos na ordem
    def run(self) -> None:

        self._exists()
        self._sql()
        self._query()

            


    

    

    
        


