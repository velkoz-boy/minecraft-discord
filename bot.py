from config import get_config
from discord_client import DiscordClient


config = get_config()
client = DiscordClient()
client.run(config["discord"]["token"])
