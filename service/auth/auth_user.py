"""
administra o login do usuario
"""
from service.auth.auth_jwt import AuthUser
from service.db.control_db import control_db

class LoginUser:

    def __init__(self)-> None:

        self.auth = AuthUser()

        

    #confere se o usuario existe, se não existir, cria a conta
    def create_account(self, email:str, password:str, name:str) -> str|None:

        user = control_db.users.select(search="email", value=email)

        if user is not None:

            return None

        user = control_db.users.insert(name=name, email=email, password=password)

        token = self.auth.create(id=user["id"], name=user["name"])

        return token

    #entra na conta do usuario
    def login_account(self, email:str, password:str) -> dict|bool:

        user = control_db.users.select(search="email", value=email)
        
        if user is not None:
        
                return "exists"

        if password == user["password"]:

         self.auth.create(id=user["id"], name=user["name"])

         return user

        return False

    #Atualiza a senha
    def update_password(self, id:int, new_password:str, user:dict) -> bool:

        if new_password != user["password"]:

            return False

        control_db.users.update(Set="password", value=new_password, id=id)

        return True

    #Deleta a conta
    def delete_account(self, id:int, password:str, user:dict) -> bool:

        if password != user["password"]:

            return False

        control_db.users.delete(id=id)

        return True


         






        

