import json
import valve.rcon

address = ("192.168.1.37", 25575)
password = "123123123"

class MinecraftRCON():
    def __init__(self, address, password, port=25575):
        self.address = address
        self.password = password
        self.port = port

    def command(self, commands, content):
        raw_commands = ' '.join(commands)
        with valve.rcon.RCON((self.address, self.port), self.password) as rcon:
            print("[#try execute]")  # TODO: logger
            rcon.execute("/{} {}".format(raw_commands, content), block=False)
            print("[executed] " + "/{} {}".format(raw_commands, content))  # TODO: logger

    def send(self, content):
        message = {"text": content}
        self.command(["tellraw", "@a"], json.dumps(message))