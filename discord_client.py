import discord

from config import get_config
from minecraft_rcon import MinecraftRCON
from observer import observe_chat


config = get_config()
mcrcon = MinecraftRCON(config["rcon"]["address"], config["rcon"]["password"])


class DiscordClient(discord.Client):
    async def on_ready(self):
        self.loop.create_task(observe_chat(config["minecraft"]["log_dir"], self))
        print("チャット連携開始")

    async def on_message(self, message):
        if message.author == self.user:
            return

        channel = self.get_channel(config["discord"]["channel"])
        if message.content and message.channel == channel:
            mcrcon.chat(message.author.nick, message.content)
