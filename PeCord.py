from json import load
from sys import exit
from time import sleep
from XeLib import cls, printer
from os import startfile
import discum
from datetime import datetime

startfile("PeCordTypes.py")

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
    print("Currently on " + str(gid) + "\n"
          "─────────┬─────────────────────────────────────────────")

@bot.gateway.command
def getmsg(resp):
    if resp.event.message:
        m = resp.parsed.auto()
        if m['channel_id'] == str(gid):
            print(str(datetime.now().strftime("%H:%M:%S")) + " │ " + str(m['author']['username']) + " " + str(m['content']))

bot.gateway.run(auto_reconnect=True)