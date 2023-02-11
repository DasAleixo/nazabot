import discord
import json
from os import getenv
import dotenv

dotenv.load_dotenv('.env')

intents = discord.Intents.all()

client = discord.Client(intents=intents)

def load_json():
    file = open('Nível.json')
    return json.load(file)

def save_json(data):
    file = open('Nível.json', 'w+')
    json.dump(data, file)

@client.event 
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        mensagem = f'{member.mention} entrou no servidor!'
        await guild.system_channel.send(mensagem)

memberxp = load_json()
def get_xp_message(value:int):
    return f'Seu XP é de: {value}'


comandos = {'!regras': 'R1, R2',
            '!xp': get_xp_message}

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    mensagem = message.content
    idmembro = message.author.id
    if idmembro in memberxp:
        memberxp[idmembro] = memberxp[idmembro] + 15
    else: 
        memberxp[idmembro] = 15
    if mensagem in comandos:
        await message.channel.send(comandos[mensagem](memberxp[idmembro]))
    save_json(memberxp)


client.run(getenv('TOKENDISCORD'))
