# SuperBot
# made for SuperBot

import asyncio
import os
from pathlib import Path
from sys import argv
import time

import telethon.utils
from telethon import TelegramClient

from SuperBot import bot
from SuperBot.utils import load_module, start_assistant
from var import Var

ALIVE_NAME = os.environ.get("ALIVE_NAME")

LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)   

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot...")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialised Sucessfully...")
        print("Starting SuperBot...")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed without any errors...")
    else:
        bot.start()


import glob

if LOAD_USERBOT == True:
    path = "SuperBot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as er:
                print(er)
else:
    print("SuperBot can't load plugins, as u have disabled them.")

if LOAD_ASSISTANT == True:
    path = "SuperBot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                start_assistant(shortname.replace(".py", ""))
            except Exception as er:
                print(er)
else:
    print("SuperBot Assistant can't be loaded, as u have disabled it.")

print("SuperBot and SuperBot Assistant are Initiated Successfully. Join @SuperBotUpdates For Updates. For queries or errors, contact @SuperBot_Support.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
    
import asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from SuperBot import bot 
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
import SuperBot._core
import os
print("SuperBot is Initiated Successfully ©️ TeamSuperBot 2021")
async def madboi():
  assistant = TelegramClient("SuperBot", API_ID, API_HASH).start(bot_token=token)
  madboy = await assistant.get_me()
  MADBOY = await bot.get_me()    
  MadBoy = f"""
**Sᴏᴍᴇᴛʜɪɴɢ Hᴀᴘᴘᴇɴᴇᴅ ! Lᴇᴛs Cʜᴇᴄᴋ** 🤔 
`☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎`
**Dɪɴɢ Dᴏɴɢ...** `.\./.\` **Tɪɴɢ Tᴏɴɢ...** `./.\./` **SᴜᴘᴇʀBᴏᴛ Hᴀs Bᴇᴇɴ Dᴇᴘʟᴏʏᴇᴅ !!**
**Pɪɴɢ Pᴏɴɢ...**
**➥ Mᴀsᴛᴇʀ** `➪` **@{MADBOY.username}**
**➥ Assɪsᴛᴀɴᴛ** `➪` **@{madboy.username}**
**➥ Sᴜᴘᴘᴏʀᴛ** `➪` **@SuperBot_Support**
**➥ Cʜᴀɴɴᴇʟ** `➪` **@SuperBotOT**
**Cʜᴇᴄᴋ ᴍᴏɪ Pɪɴɢ ᴛɪᴍᴇ ʙʏ** `.ping` **[Fᴏʀ UsᴇʀBᴏᴛ] or** `/ping` **[Fᴏʀ Assɪsᴛᴀɴᴛ]**
"""
  if ALIVE_NAME:
    try:
      
      await assistant.send_message(bot.me.id, MadBoy)
    except:
       pass
  else:
    print("SuperBot Initiated Succcessfully.")
    
async def danger(username):
  i = 0
  xx = 0
  async for x in bot.iter_dialogs():
    if x.is_group or x.is_channel:
     try:
       await bot.edit_permissions(x.id, username, view_messages=False)
       i += 1
     except:
       xx += 1
  print(f"THE DANGER USER WAS BANNED IN {i-xx}")
# bot.loop.run_until_complete(danger("")) # Temporary Use
# bot.loop.run_until_complete(madboy())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
    
else:
    bot.run_until_disconnected()

# SuperBot
# made for SuperBot
