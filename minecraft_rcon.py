import json
import valve.rcon


class MinecraftRCON:
    def __init__(self, address, password, port=25575):
        self.address = address
        self.password = password
        self.port = port

    def execute(self, commands):
        raw_commands = " ".join(commands)
        with valve.rcon.RCON((self.address, self.port), self.password) as rcon:
            rcon.execute("/{}".format(raw_commands), block=False, timeout=10)

    def chat(self, author, content):
        content = "<{}> {}".format(author, content)
        print("[FromDiscord] {}".format(content))  # TODO: logger
        message = {"text": content, "color": "blue"}
        self.execute(["tellraw", "@a", json.dumps(message)])
