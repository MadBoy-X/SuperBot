# SuperBot
# made for SuperBot

# imported from ULTRA-X by madboy482

from telethon import events, Button, custom
from SuperBot import bot
from SuperBot import assistant

import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions

@assistant.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 MadBoy = event.builder
 X= [[custom.Button.inline("🔥 Cʟɪᴄᴋ Hᴇʀᴇ 🔥",data="obhai")]]
 query = event.text
 result = MadBoy.article("SᴜᴘᴇʀBᴏᴛ",text="**SᴜᴘᴇʀBᴏᴛ's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Sᴜᴘᴘᴏʀᴛ\n\n© @SuperBotOT**",buttons=X,link_preview=False)
 await event.answer([result])
 
@assistant.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):
  await event.edit(text=f"**SᴜᴘᴇʀBᴏᴛ's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Gʀᴏᴜᴘ Lɪɴᴋ\n\n© @SuperBotOT**",buttons=[
   [
    Button.url(f"⚜️ Rᴇᴘᴏ ⚜️", url="https://github.com/MadBoy-X/SuperBot"),
    Button.url(f"🌚 Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ 🌝", url="https://t.me/SuperBot_Support")
   ],
   [
    Button.url(f"🔰 Dᴇᴘʟᴏʏ 🔰", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FMadBoy-X%2FSuperBot-Deploy&template=https%3A%2F%2Fgithub.com%2FMadBoy-X%2FSuperBot-Deploy"),
    Button.url(f"💠 Sᴛʀɪɴɢ 💠", url="https://replit.com/@madboy482/SuperBot#main.py"),
   ]
  ]
                  )

# SuperBot
# made for SuperBot

# imported from ULTRA-X by madboy482
