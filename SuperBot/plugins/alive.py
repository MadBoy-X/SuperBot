# THANKS TO MADBOY482
# MADE BY JASSMANAK1125 AND MADBOY482
# Kang with credits else gay...
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from SuperBot.utils import admin_cmd, sudo_cmd
from SuperBot import ALIVE_NAME, Lastupdate
from . import dcdef
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ֆʊքɛʀɮօȶ"


# alive.py for ֆʊքɛʀɮօȶ
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/6aa39732748ed7c319943.jpg"
file2 = "https://telegra.ph/file/a6d72504bc09e71484a54.jpg"
file3 = "https://telegra.ph/file/3cdbede1d5d85aa2d50fc.jpg"
file4 = "https://telegra.ph/file/3dae01973943e8b28c931.jpg"
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "**ꜱᴜᴘᴇʀʙᴏᴛ ɪꜱ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴏɴ ꜰɪʀᴇ**\n\n"
    pm_caption += "**ʏᴇꜱ ᴍᴀꜱᴛᴇʀ, ᴀᴍ ᴀʟɪᴠᴇ ᴀɴᴅ ꜱʏꜱᴛᴇᴍꜱ ᴀʀᴇ ᴡᴏʀᴋɪɴɢ ᴘᴇʀꜰᴇᴄᴛʟʏ**\n\n"
    pm_caption += "✘ ᴀʙᴏᴜᴛ ᴍʏ ꜱʏꜱᴛᴇᴍ ✘\n\n"
    pm_caption += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ {version.__version__}\n"
    pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/SuperBot_Support)\n"
    pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [ᴛᴇᴀᴍ ꜱᴜᴘᴇʀʙᴏᴛ](https://github.com/MadBoy-X)\n"
    pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [ꜱᴜᴘᴇʀʙᴏᴛ](https://github.com/MadBoy-X/SuperBot)\n"
    pm_caption += :➾ **ʀᴇᴘᴏ** ☞ [ꜱᴜᴘᴇʀʙᴏᴛ](https://github.com/MadBoy-X/SuperBot)\n\n" 
    pm_caption += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ {uptime}\n\n"
    pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    
