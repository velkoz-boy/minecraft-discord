import discord
import yaml

#from tail import tail
from minecraft_rcon import MinecraftRCON


with open("config.yaml", "r") as yml:
    config = yaml.safe_load(yml)

client = discord.Client()
mcrcon = MinecraftRCON(config["rcon"]["address"], config["rcon"]["password"])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #tail(r"./server/logs/latest.log")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content:
        mcrcon.chat(message.author.name, message.content)

client.run(config["discord"]["token"])