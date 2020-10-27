import discord
import yaml
from minecraft_rcon import MinecraftRCON

with open("config.yaml", "r") as yml:
    config = yaml.safe_load(yml)

client = discord.Client()
mcr = MinecraftRCON(config["rcon"]["address"], config["rcon"]["password"])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content:
        mcr.send("<{}> ".format(message.author.name) + message.content)
        #await message.channel.send('Hello!')

client.run(config["discord"]["token"])