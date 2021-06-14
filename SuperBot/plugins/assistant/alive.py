# SuperBot
# made for SuperBot 

# imported from ULTRA-X by madboy482

# COPYRIGHT (C) 2021-2022 BY LEGENDX22
# modify by madboy482 and alain_champion

from SuperBot import bot
from SuperBot import assistant
import heroku3
from telethon import events
from SuperBot import StartTime
import time
import datetime
from . import *
from telethon import events, Button, custom
import re, os
from SuperBot import assistant
from SuperBot import bot

BOT = "𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕"

@assistant.on(events.NewMessage(pattern=("/alive")))
async def awake(event):
  MADBOY = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
  MADBOY += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
  MADBOY += f"**{BOT} Vᴇʀsɪᴏɴ** : `1.0.1`\n\n"
  MADBOY += f"**Usᴇʀ** : @{bot.me.username}\n\n"
  MADBOY += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
  MADBOY += "**Tᴇʟᴇᴛʜᴏɴ** : `1.21.1`\n\n"
  MADBOY += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
  BUTTON = [[Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/MadBoy-X/SuperBot")]]
  BUTTON += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="MADBOY")]]
  await assistant.send_file(event.chat_id, PHOTO, caption=MADBOY,  buttons=BUTTON)




@assistant.on(events.callbackquery.CallbackQuery(data=re.compile(b"MADBOY")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOY22 🔥
  MADBOYX = [[Button.url("Rᴇᴘᴏ SᴜᴘᴇʀBᴏᴛ", "https://github.com/MadBoy-X/SuperBot")]]
  MADBOYX +=[[Button.url("Dᴇᴘʟᴏʏ SᴜᴘᴇʀBᴏᴛ", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FMadBoy-X%2FSuperBot-Deploy&template=https%3A%2F%2Fgithub.com%2FMadBoy-X%2FSuperBot-Deploy")]]
  MADBOYX +=[[Button.url("Tᴜᴛᴏʀɪᴀʟ", ""), Button.url("Sᴛʀɪɴɢ Sᴇssɪᴏɴ", "https://replit.com/@madboy482/SuperBot#main.py")]]
  MADBOYX +=[[Button.url("Aᴘɪ Iᴅ & Aᴘɪ Hᴀsʜ", "https://t.me/API_ScrapperBot"), Button.url("Rᴇᴅɪs", "https://redislabs.com")]]
  MADBOYX +=[[Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ", "https://t.me/SuperBotOT"), Button.url("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", "https://t.me/SuperBot_Support")]]
  MADBOYX +=[[custom.Button.inline("«« Aʟɪᴠᴇ", data="MADBOI")]]
  await event.edit(text=f"Aʟʟ Dᴇᴛᴀɪʟs Oғ Rᴇᴘᴏs", buttons=MADBOYX)


@assistant.on(events.callbackquery.CallbackQuery(data=re.compile(b"MADBOI")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOY22 🔥
  MADBOY = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
  MADBOY += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
  MADBOY += f"**{BOT} Vᴇʀsɪᴏɴ** : `1.0.1`\n\n"
  MADBOY += f"**Usᴇʀ** : @{bot.me.username}\n\n"
  MADBOY += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
  MADBOY += "**Tᴇʟᴇᴛʜᴏɴ** : `1.21.1`\n\n"
  MADBOY += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
  BUTTONS = [[Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/MadBoy-X/SuperBot")]]
  BUTTONS += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="MADBOY")]]
  await event.edit(text=MADBOY, buttons=BUTTONS)


@assistant.on(events.NewMessage(pattern=("/repo")))
async def repo(event):
  await assistant.send_message(event.chat, "**Hᴇʀᴇ Is Tʜᴇ Rᴇᴘᴏ Fᴏʀ Sᥙρҽɾẞσ𝜏** \n\nFᴏʀ Aɴʏ Hᴇʟᴘ :- @SuperBotOT", buttons=[[Button.url("⚜️ Rᴇᴘᴏ ⚜️", "https://github.com/MadBoy-X/SuperBot"), Button.url("🔰 Dᴇᴘʟᴏʏ 🔰", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FMadBoy-X%2FSuperBot-Deploy&template=https%3A%2F%2Fgithub.com%2FMadBoy-X%2FSuperBot-Deploy")]])


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@assistant.on(events.NewMessage(pattern=None))
async def ok(event):
    msg = str(event.text)
    if not msg == "/ping":
     return

    start_time = datetime.datetime.now()
    message = await event.reply("_.._.._Pinging_.._.._")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b><i>☞ Pᴏɴɢ !!</i></b>\n"
        "<b>➥ Tɪᴍᴇ Tᴀᴋᴇɴ:</b> <code>{}</code>\n"
        "<b>➥ Sᴇʀᴠɪᴄᴇ Uᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )
    
# SuperBot
# made for SuperBot 

# imported from ULTRA-X by madboy482
