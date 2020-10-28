import discord

from config import get_config
from minecraft_rcon import MinecraftRCON


config = get_config()
mcrcon = MinecraftRCON(config["rcon"]["address"], config["rcon"]["password"])


class DiscordClient(discord.Client):
    async def on_ready(self):
        print("チャット連携開始")

    async def on_message(self, message):
        if message.author == self.user:
            return

        channel = self.get_channel(config["discord"]["channel"])
        if message.content and message.channel == channel:
            mcrcon.chat(message.author.name, message.content)
