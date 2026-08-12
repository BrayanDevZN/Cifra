"""
faz a requisição pra open ai
"""


from openai import OpenAI

class Response:

    def __init__(self, mensage:str, prompt:str, key:str=None)-> None:

        
        self.msg = mensage

        #Objeto da classe
        self.client = OpenAI(api_key=key)

        #Prompt pro modelo
        self.prompt = prompt

       
    #Faz a requisição e retorna a responsta em streaming
    def get(self) -> str:

        try:

            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": self.prompt},
                    {"role": "user", "content": self.msg}
                ],
                model="gpt-4o-mini",
                stream=False
            )



            response = response.choices[0].message.content

           
                

            return response

        except Exception as e:
            raise (e)







        