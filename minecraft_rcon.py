import json
import valve.rcon


class MinecraftRCON():
    def __init__(self, address, password, port=25575):
        self.address = address
        self.password = password
        self.port = port

    def command(self, commands, content):
        raw_commands = ' '.join(commands)
        with valve.rcon.RCON((self.address, self.port), self.password) as rcon:
            rcon.execute("/{} {}".format(raw_commands, content), block=False)
            print("[fromDiscord]" + "/{} {}".format(raw_commands, content))  # TODO: logger

    def chat(self, author, content):
        content = "<{}§9@Discord§f> {}".format(author, content)
        message = {"text": content}
        self.command(["tellraw", "@a"], json.dumps(message))