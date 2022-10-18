from json import load
from sys import exit
from time import sleep
from XeLib import cls, printer
import discum
from datetime import datetime

cls()
printer.lprint("Authenticating with your account...")
with open('settings.PeC.json') as c:
    v = load(c)
    token = str(v["Token"])
    gid = str(v["ChannelID"])
    printer.lprint("Success!")
    bot = discum.Client(token=token, log=False)
    sleep(1)
    cls()

while True:
    msg = input("> ")
    bot.sendMessage(str(gid), msg)

bot.gateway.run(auto_reconnect=True)