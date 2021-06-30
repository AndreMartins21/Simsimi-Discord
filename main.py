import discord  
from simsimi import *

client = discord.Client()


@client.event
async def on_message(msg):

  canais = ["simsimi"] # Inserir o nome dos canais para o bot responder
  
  message = msg.content.lower() # Salvar a mensagem digitada pelo usuário pelo Discord 
  
  if msg.author.bot: 
    '''
    Se a mensagem for de um bot, não irá responder
    '''
    return
  
  if msg.channel.name in canais:
    resposta = simsimi(message)
    await msg.channel.send(resposta) # Enviará a resposta do Simsimi ao chat em que a mensagem foi encaminhada


@client.event
async def on_ready():
  print(f"{client.user} está online!")

client.run("INSIRA_O_TOKEN_DO_BOT")
