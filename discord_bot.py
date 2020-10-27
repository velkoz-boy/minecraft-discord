import discord
import minecraft_rcon

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content:
        mcr = minecraft_rcon.MinecraftRCON("192.168.1.37", "123123123")
        mcr.send("<{}> ".format(message.author.name) + message.content)
        #await message.channel.send('Hello!')

client.run('NjQwMDk2MzY3Njk1NjI2MjQw.Xb02Mg.W9kMFyvmMRoJjQ-wETjiNV62tyQ')