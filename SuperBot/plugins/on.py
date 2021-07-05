# Thanks to @Shivam_Patel Bro
# Thanks to Sipak .. 
# Idea by @Shivam_Patel 
# Made by @Shivam_Patel & @ProgrammingError ....TEAM DC
# Kang with credits else gay...
# inline alive
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from SuperBot.utils import admin_cmd
from SuperBot import ALIVE_NAME, Lastupdate
from . import dcdef
from SuperBot import bot as borg
from telethon.tl.custom import Button
from telethon.tl.types import ChannelParticipantsAdmins
global ok
ok = borg.uid

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SuperBot"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO" , None)

TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await borg.get_me()
        uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
        dc_text=(f"**✧✧ 𝙎𝙪𝙥𝙚𝙧𝘽𝙤𝙩 𝙞𝙨 𝙐𝙥 𝙖𝙣𝙙 𝙍𝙪𝙣𝙣𝙞𝙣𝙜 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 ✧✧**\n\n**𝑨𝒍𝒍 𝒕𝒉𝒆 𝑺𝒚𝒔𝒕𝒆𝒎𝒔 𝒂𝒏𝒅 𝑫𝒂𝒕𝒂𝑩𝒂𝒔𝒆𝒔 𝒂𝒓𝒆 𝑭𝒖𝒏𝒄𝒕𝒊𝒐𝒏𝒊𝒏𝒈 𝑷𝒓𝒐𝒑𝒆𝒓𝒍𝒚, 𝒂𝒔 𝒕𝒉𝒆𝒚 𝒔𝒉𝒐𝒖𝒍𝒅 𝒅𝒐.**\n\n✘ 𝐼𝑛𝑓𝑜 𝐴𝑏𝑜𝑢𝑡 𝑀𝑦 𝑆𝑦𝑠𝑡𝑒𝑚 ✘\n\n➥ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀꜱɪᴏɴ :** `{version.__version__}`\n➥ **Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ :** [Jᴏɪɴ](https://t.me/SuperBot_SupportChat)\n➥ **Cᴏᴘʏʀɪɢʜᴛ Bʏ :** [𝐒𝐮𝐩𝐞𝐫𝐁𝐨𝐭](https://github.com/MadBoy-X/SuperBot)\n\n➥ **Uᴘᴛɪᴍᴇ :** `{uptime}`\n\n➥ **Mʏ Mᴀsᴛᴇʀ :** [{DEFAULTUSER}](tg://user?id={ok})\n")
        if query.startswith("alive") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Repo", "https://github.com/MadBoy-X/SuperBot"),
                    Button.url("Deploy", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FMadBoy-X%2FSuperBot-Deploy&template=https%3A%2F%2Fgithub.com%2FMadBoy-X%2FSuperBot-Deploy")],
                    [Button.url("String", "https://replit.com/@madboy482/SuperBot#main.py"),
                    Button.url("Support", "https://t.me/SuperBot_SupportChat"),
                ]
            ]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="SuperBot",
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="SuperBot",
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)
