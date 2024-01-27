import json
import discord
from discord.ui import View, Modal, InputText
from discord.ext import commands
from utils import DataManager

intents = discord.Intents().all()
client = commands.Bot(command_prefix = '!', case_insensitive = False, help_command=None, intents=intents)
data = DataManager(file='db.json')

@client.event
async def on_ready():
    print('Bot Online!')
    client.add_view(view=Buttons())

class Buttons(View):
    """
    Classe responsável pelos callback dos botões
    """
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Adicionar convidado', emoji='➕', style=discord.ButtonStyle.green, custom_id='add_conv')
    async def callback_add(self, button, inter: discord.Interaction):
        modal = input_user()
        await inter.response.send_modal(modal)
        await modal.wait()
        if await data.add_user(user=modal.value):
            await inter.followup.send(f'**✅ Sucesso!** Você adicionou: `{modal.value}` como convidado.', ephemeral=True)
        else:
            await inter.followup.send(f'**❌ ERRO!** O usuário: `{modal.value}` já está adicionado na lista.', ephemeral=True)

    @discord.ui.button(label='Remover convidado', emoji='➖', style=discord.ButtonStyle.red, custom_id='rem_conv')
    async def callback_rem(self, button, inter: discord.Interaction):
        modal = input_user()
        await inter.response.send_modal(modal)
        await modal.wait()
        if await data.remove_user(user=modal.value):
            await inter.followup.send(f'**✅ Sucesso!** Você removeu: `{modal.value}` da lista de convidados.', ephemeral=True)
        else:
            await inter.followup.send(f'**❌ ERRO!** O usuário: `{modal.value}` não está adicionado na lista.', ephemeral=True)

    @discord.ui.button(label='Checar convidado', emoji='🔎', style=discord.ButtonStyle.blurple, custom_id='find_user')
    async def callback_checkuser(self, button, inter: discord.Interaction):
        modal = input_user()
        await inter.response.send_modal(modal)
        await modal.wait()
        nomes = await data.find_users(user=modal.value)
        if nomes:
            embed = discord.Embed(title='Checar convidado', color=discord.Colour.green(),
                        description=f'**Exibindo abaixo todos os nomes adicionados que comecem com: `{modal.value}`**\n')
            nomes.sort()
            for name in nomes:
                embed.description += f'\n> - {name}'
            await inter.followup.send(embed=embed, ephemeral=True)
        else:
            await inter.followup.send(f'**❌ ERRO!** Não foi possível encontrar ninguém que comece com: `{modal.value}`.'
            '\n**OBS:** Se certifique-se de ter adicionado a acentuação necessária no nome.', ephemeral=True)

    @discord.ui.button(label='Visualizar lista', emoji='📁', style=discord.ButtonStyle.blurple, custom_id='see_list')
    async def callback_listall(self, button, inter: discord.Interaction):
        embed = discord.Embed(title='Lista de convidados', color=discord.Colour.blurple(),
                    description='**Lista de todos os convidados adicionados')
        users = await data.get_all_users()
        users.sort()
        qnt = 0
        if users != ['Nenhum convidado registrado.']:
            qnt = len(users)
        embed.description += f' - Total: {qnt}**'
        for conv in users:
            embed.description += f'\n- {conv}'

        await inter.response.send_message(embed=embed, ephemeral=True)

class input_user(Modal):
    def __init__(self):
        super().__init__(title='Gerenciador de Convidados', timeout=600)
        self.value = None
        self.add_item(InputText(label='Digite o nome completo do convidado abaixo',
                                style=discord.InputTextStyle.short,
                                required=True, min_length=4, max_length=35))

    async def callback(self, inter: discord.Interaction):
        await inter.response.defer()
        self.value = self.children[0].value
        self.stop()


@client.slash_command(description='Gerenciador da lista de convidados', guild_only=True)
async def lista(ctx):
    embed = discord.Embed(title='Gerenciador de convidados', color=discord.Colour.green(),
                          description='**- Adicionar convidado:** `Adiciona uma nova pessoa na lista de convidados`\n'
                          '**- Remover convidado:** `Remove uma pessoa que está adicionada na lista de convidados`\n'
                          '**- Checar convidado:** `Consulta se um nome está na lista de convidados`\n'
                          '**- Visualizar lista:** `Visualiza a lista inteira de convidados`\n\n')
    await ctx.respond(embed=embed, view=Buttons())

def load_config():
    try:
        with open('config.json') as f:
            config = json.load(f)
            token = config.get('token')
            if not token:
                raise ValueError("ERRO! Não foi possível encontrar o token. Verifique seu arquivo config.json")
            return token
    except FileNotFoundError:
        raise FileNotFoundError("ERRO! O arquivo config.json não existe. Confira seus arquivos.")
    except json.JSONDecodeError:
        raise ValueError("ERRO! Não foi possível decodificar o arquivo de configuração JSON.")

if __name__ == '__main__':
    token = load_config()
    try:
        client.run(token)
    except (discord.errors.LoginFailure, discord.errors.HTTPException):
        print("ERRO! Token inválido. Verifique se o token inserido no config.json é válido.")