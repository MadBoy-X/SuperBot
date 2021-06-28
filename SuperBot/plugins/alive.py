# SuperBot
# made for SuperBot

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
from . import sbdef
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Sᥙρҽɾẞσ𝜏"

global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/9dac29dbb00b90b17537e.png"
file2 = "https://telegra.ph/file/7599a1eadb71eeaa18817.png"
file3 = "https://telegra.ph/file/c57af3507a644bc1344ba.png"
file4 = "https://telegra.ph/file/9b2e2d708740364c6eaf4.png"
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await sbdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "**✧✧ 𝙎𝙪𝙥𝙚𝙧𝘽𝙤𝙩 𝙞𝙨 𝙐𝙥 𝙖𝙣𝙙 𝙍𝙪𝙣𝙣𝙞𝙣𝙜 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 ✧✧**\n\n"
    pm_caption += "**𝑨𝒍𝒍 𝒕𝒉𝒆 𝑺𝒚𝒔𝒕𝒆𝒎𝒔 𝒂𝒏𝒅 𝑫𝒂𝒕𝒂𝑩𝒂𝒔𝒆𝒔 𝒂𝒓𝒆 𝑭𝒖𝒏𝒄𝒕𝒊𝒐𝒏𝒊𝒏𝒈 𝑷𝒓𝒐𝒑𝒆𝒓𝒍𝒚, 𝒂𝒔 𝒕𝒉𝒆𝒚 𝒔𝒉𝒐𝒖𝒍𝒅 𝒅𝒐.**\n\n"
    pm_caption += "✘ 𝐼𝑛𝑓𝑜 𝐴𝑏𝑜𝑢𝑡 𝑀𝑦 𝑆𝑦𝑠𝑡𝑒𝑚 ✘\n\n"
    pm_caption += f"➥ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀꜱɪᴏɴ :** {version.__version__}\n"
    pm_caption += "➥ **Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ :** [Jᴏɪɴ](https://t.me/superbotprojects)\n"
    pm_caption += "➥ **Cᴏᴘʏʀɪɢʜᴛ Bʏ :** [𝐒𝐮𝐩𝐞𝐫𝐁𝐨𝐭](https://github.com/MadBoy-X/SuperBot)\n\n"
    pm_caption += f"➥ **Uᴘᴛɪᴍᴇ :** {uptime}\n\n"
    pm_caption += f"➥ **Mʏ Mᴀsᴛᴇʀ :** [{DEFAULTUSER}](tg://user?id={ghanti})\n"
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
    
# SuperBot
# made for SuperBot
