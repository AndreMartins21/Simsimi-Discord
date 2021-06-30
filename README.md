<div style="display: inline_block">
  <img align="center" alt="Discord" src="https://github.com/AndreMartins21/Simsimi-no-Discord/blob/main/Images/discord_logo.png" width="150" height="150">
  <img align="center" alt="Simsimi" src="https://github.com/AndreMartins21/Simsimi-no-Discord/blob/main/Images/Logo%20Simsimi.png" width="150" height="150">
  
</div>

# <> BOT DISCORD + SIMSIMI  

  Trata-se de um script que implementa uma API do chat-bot [Simsimi](https://www.simsimi.com/) em um bot associado à plataforma do [Discord](https://discord.com/).
  
## Tecnologias Utilizadas::

**|->** [Python V3.9](https://www.python.org/): Linguagem de programação versátil e de alto nível;

**|->** [Requests](https://docs.python-requests.org/en/master/): Librabry de requisição HTTP (será usada para acessar a API do Simsimi)

**|->** [Discord.py V1.7.1](https://discordpy.readthedocs.io/en/stable/) = Library para a integração com o Discord


## Instruções:

- Instalar a biblioteca **discord.py**:
```
pip install discord.py
```

- No arquivo [main.py](https://github.com/AndreMartins21/Simsimi-Discord/blob/main/main.py) está contido toda a esquematização do bot. Nesse, você deve modificar dois objetos: 

    [canais (list)](https://github.com/AndreMartins21/Simsimi-Discord/blob/01fb7c2ae741aad65395eecc99822f8aea27a5fc/main.py#L10) = Adicionar à lista os canais nos quais a integração simsimi poderá responder;

    [TOKEN (str)](https://github.com/AndreMartins21/Simsimi-Discord/blob/a60bd59b0e6e6ff9b7ce79e746ae3f2dbe65641d/main.py#L29) = Inserir o TOKEN do bot. 

- No arquivo [simsimi.py](https://github.com/AndreMartins21/Simsimi-Discord/blob/main/simsimi.py) está presente uma função que realiza a integração da mensagem requerida no discord com a API do Simsimi.
