import discord as asyncio
import discord

import SECRETS

client = discord.Client()


@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')
    await client.change_presence(game=discord.Game(name='mit Strings und Variablen', type=0))

    @client.event
    @asyncio.coroutine
    def on_message(message):
        print(message.content + " - " + message.author.name)


client.run(SECRETS.TOKEN)
