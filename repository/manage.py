"""
junta os modulos de repository
"""


#Cria uma interface pro controle de banco de dados
from repository.db.actions import ActionsDb
from repository.db.conversation import ConversationDb
from repository.db.chats import ChatsDb
from repository.db.users import UsersDb

from sqlalchemy import Engine


class ControlDb:

    def __init__(self, engine: Engine)-> None:

        self.users = UsersDb(engine=engine)
        self.conversation = ConversationDb(engine=engine)
        self.chats = ChatsDb(engine=engine)
        self.actions = ActionsDb(engine=engine)





from repository.file.session import SessionJson
from repository.file.prompt import read
        