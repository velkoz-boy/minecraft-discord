import valve.rcon

address = ("192.168.1.37", 25575)
password = "123123123"
with valve.rcon.RCON(address, password) as rcon:
    response = rcon.execute("/say hello")
    print(response.text)