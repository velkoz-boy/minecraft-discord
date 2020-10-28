from config import get_config
from discord_client import DiscordClient
from tail import observe_chat


config = get_config()
client = DiscordClient()
client.loop.create_task(observe_chat(config["minecraft"]["log_dir"], client))
client.run(config["discord"]["token"])
