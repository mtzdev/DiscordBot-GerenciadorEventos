import json
from typing import Union, List

class DataManager:
    def __init__(self, file: str):
        self.dbfile = file

    async def get_data(self):
        try:
            with open(self.dbfile, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print(f'ERRO! Arquivo {self.dbfile} não encontrado.')
            return

    async def save_data(self, new_data):
        if not isinstance(new_data, dict):
            print('ERRO save_data! Data recebida não é do tipo dict.')
            return

        try:
            with open(self.dbfile, 'w') as f:
                json.dump(new_data, f, indent=4)
            return True
        except json.JSONDecodeError:
            print('ERRO! Novo dado não foi serializado corretamente.')
            return
        except IOError as e:
            print(f'ERRO! {e}')
            return

    async def add_user(self, user: str) -> bool:
        data: dict = await self.get_data()
        user = user.title()

        if user in data['convidados']:
            return False

        data['convidados'].append(user)
        await self.save_data(data)
        return True

    async def remove_user(self, user: str) -> bool:
        data: dict = await self.get_data()
        user = user.title()

        if user not in data['convidados']:
            return False

        data['convidados'].remove(user)
        await self.save_data(data)
        return True

    async def find_users(self, user: str) -> Union[List[str], bool]:
        data: dict = await self.get_data()
        user = user.title()

        nomes = [n for n in data['convidados'] if n.startswith(user)]
        if len(nomes) > 0:
            return nomes
        else:
            return False

    async def get_all_users(self) -> List[str]:
        data: dict = await self.get_data()
        if len(data['convidados']) > 0:
            return data['convidados']
        else:
            return ['Nenhum convidado registrado.']
