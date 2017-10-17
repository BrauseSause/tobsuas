import asyncio
import io
import random
import discord
import requests

client = discord.Client()
sbid = "215748669784195073"

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')

@client.event
async def on_message(message):
    try:
        if message.mentions[0]:
            user = message.mentions[0]
            id = user.id
            if id == sbid:
                await client.delete_message(message)
                await client.send_message(message.channel, "Bitte SauseBrause nicht taggen! Abfuckschutz aktiviert.")
    except Exception as error:
        print("Erwarteter Error: {error}".format(error=error))

client.run('MzQ2OTk3MTY5MDcwMjc2NjA4.DHR94g.It1hLi-Tk-tEAKln3VWg5MSQVAk')