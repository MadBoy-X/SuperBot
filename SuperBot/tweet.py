# SuperBot
# made for SuperBot

import os
import re
import urllib.request
import PIL.ImageOps
import requests
from PIL import Image, ImageDraw, ImageFont
from validators.url import url

async def moditweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=narendramodi"
    ).json()
    SUPER = r.get("message")
    BOT = url(SUPER)
    if not BOT:
        return "Check Syntax Once More !!"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(SUPER).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"


async def sunnytweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=sunnyleone"
    ).json()
    SUPER = r.get("message")
    BOT = url(SUPER)
    if not BOT:
        return "Check Syntax Once More !!"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(SUPER).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"

async def johnnytweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=johnnysins"
    ).json()
    SUPER = r.get("message")
    BOT = url(SUPER)
    if not BOT:
        return "Check Syntax Once More !!"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(SUPER).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"

async def bhautweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=hindustanibhau"
    ).json()
    SUPER = r.get("message")
    BOT = url(SUPER)
    if not BOT:
        return "Check Syntax Once More !!"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(SUPER).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"

async def jtweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=the_joker"
    ).json()
    SUPER = r.get("message")
    BOT = url(SUPER)
    if not BOT:
        return "Check Syntax Once More !!"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(SUPER).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"

async def miatweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=miakhalifa"
    ).json()
    SUPER = r.get("message")
    BOT = url(SUPER)
    if not BOT:
        return "Check Syntax Once More !!"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(SUPER).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"

# SuperBot
# made for SuperBot
