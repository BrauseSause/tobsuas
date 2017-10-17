import random

import discord as asyncio
import discord

import Daten
import SECRETS
import cmd_ping

client = discord.Client()

commands = {
    "ping": cmd_ping,

}


@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print("SauseBot hat sich auf diesen Servern eingeloggt: \n")
    print('------------------------')
    await client.change_presence(game=discord.Game(name='mit Strings und Variablen', type=0))

    @client.event
    async def on_message(message):
        # Coinflip
        if message.content.lower().startswith(Daten.PREFIX):
            choice = random.randint(1, 2)
            if choice == 1:
                await client.add_reaction(message, '🌑')
            if choice == 2:
                await client.add_reaction(message, '🌕')

    @client.event()
    @asyncio.coroutine
    def on_message(message):
        if message.content.startswith(Daten.PREFIX):
            invoke = message.content[len(Daten.PREFIX):].split(" ")[0]
            args = message.content.slit(" ")[1:]
            print("INVOKE: %s\nARGS: %s" % (invoke, args.__str__ ()[1:-1]).replace("", ""))




client.run(SECRETS.TOKEN)
