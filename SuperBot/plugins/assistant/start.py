# SuperBot
# made for SuperBot 

#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import asyncio
import io
import re

from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest

from SuperBot import bot
from SuperBot import assistant
from SuperBot import ALIVE_NAME
from SuperBot.plugins.sql_helper.blacklist_assistant import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from SuperBot.plugins.sql_helper.botusers_sql import add_me_in_db, his_userid
from SuperBot.plugins.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Sᥙρҽɾẞσ𝜏"

@assistant.on(events.NewMessage(pattern="^/start"))
async def start(event):
    starkbot = await assistant.get_me()
    bot_id = starkbot.first_name
    bot_username = starkbot.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    vent = event.chat_id
    starttext = f"Hello, **{firstname}**!!\nNice To Meet You 🤗 !!\nI guess, that you know me, Uhh you don't, np..\nWell I'm **{bot_id}**.\n\n**A Pᴏᴡᴇʀғᴜʟ Assɪᴛᴀɴᴛ Oғ** [{DEFAULTUSER}](tg://user?id={bot.uid})\n\n                           **Pᴏᴡᴇʀᴇᴅ Bʏ** [Sᥙρҽɾẞσ𝜏](t.me/SuperBotOT)\n\n**Yᴏᴜ Cᴀɴ Cʜᴀᴛ Wɪᴛʜ Mʏ Mᴀsᴛᴇʀ Tʜʀᴏᴜɢʜ Tʜɪs Bᴏᴛ.**\n**Iғ Yᴏᴜ Wᴀɴᴛ Yᴏᴜʀ Oᴡɴ Assɪᴛᴀɴᴛ, Yᴏᴜ Cᴀɴ Dᴇᴘʟᴏʏ Fʀᴏᴍ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ.**"
    if event.sender_id == bot.uid:
        await assistant.send_message(
            vent,
            message=f"𝑯𝒆𝒚𝒂❗❗ 𝑴𝒂𝒔𝒕𝒆𝒓❗❗ 𝑰𝒕❜𝒔 𝒎𝒆 {bot_id}, 𝒀𝒐𝒖𝒓 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 !!\n𝑾𝒉𝒂𝒕 𝒚𝒐𝒖 𝒘𝒂𝒏𝒏𝒂 𝒅𝒐 𝒕𝒐𝒅𝒂𝒚 ??",
            buttons=[
                [custom.Button.inline("Bᴏᴛ Usᴇʀs 🔥", data="users")],
                [custom.Button.inline("Mʏ Cᴏᴍᴍᴀɴᴅs ⚙️", data="gibcmd")],
                [
                    Button.url(
                        "Iɴᴠɪᴛᴇ Mᴇ Tᴏ A Gʀᴏᴜᴘ 👥", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await assistant.send_message(
            event.chat_id,
            message=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("Dᴇᴘʟᴏʏ ʏᴏᴜʀ SᴜᴘᴇʀBᴏᴛ", data="deploy")],
                [Button.url("Gᴇᴛ Hᴇʟᴘ ❓", "https://t.me/SuperBot_Support")],
            ],
        )


# Data's


@assistant.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await assistant.send_message(
            event.chat_id,
            message="𝒀𝒐𝒖 𝒄𝒂𝒏 𝑫𝒆𝒑𝒍𝒐𝒚 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕 𝒐𝒏 𝑯𝒆𝒓𝒐𝒌𝒖 𝒃𝒚 𝒇𝒐𝒍𝒍𝒐𝒘𝒊𝒏𝒈 𝒕𝒉𝒆 𝑺𝒕𝒆𝒑𝒔 𝒃𝒆𝒍𝒐𝒘, 𝒀𝒐𝒖 𝒄𝒂𝒏 𝒔𝒆𝒆𝒌 𝒇𝒐𝒓 𝑯𝒆𝒍𝒑 𝒐𝒏 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑮𝒓𝒐𝒖𝒑.\n𝑻𝒉𝒂𝒏𝒌𝒔 𝒇𝒐𝒓 𝑪𝒐𝒏𝒕𝒂𝒄𝒕𝒊𝒏𝒈 𝑴𝒆.",
            buttons=[
                [Button.url("Dᴇᴘʟᴏʏ Tᴜᴛᴏʀɪᴀʟ 📺", "")],
                [Button.url("Gᴇᴛ Hᴇʟᴘ ❓", "https://t.me/SuperBot_Support")],
            ],
        )


@assistant.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        total_users = get_all_users()
        users_list = "List Of Total Users In Bot. \n\n"
        for starked in total_users:
            users_list += ("==> {} \n").format(int(starked.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await assistant.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="Tᴏᴛᴀʟ Usᴇʀs ᴏғ Yᴏᴜ Assɪsᴛᴀɴᴛ Bᴏᴛ.",
                allow_cache=False,
            )
    else:
        pass


@assistant.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    await event.delete()
    grabon = "**Hᴇʏᴀ!! Bᴇʟᴏᴡ ᴀʀᴇ sᴏᴍᴇ ᴏғ Mʏ Cᴏᴍᴍᴀɴᴅs :**\n➤ /start - 𝘾𝙝𝙚𝙘𝙠 𝙞𝙛 𝙄 𝙖𝙢 𝘼𝙡𝙞𝙫𝙚\n➤ /ping - 𝙋𝙤𝙣𝙜 !\n➤ /tr <lang-code> - 𝙏𝙧𝙖𝙣𝙨𝙡𝙖𝙩𝙚 𝙖 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙡𝙖𝙣𝙜𝙪𝙖𝙜𝙚\n➤ /broadcast - 𝙎𝙚𝙣𝙙𝙨 𝙖 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙏𝙤 𝙖𝙡𝙡 𝙐𝙨𝙚𝙧𝙨 𝙄𝙣 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘽𝙤𝙩\n➤ /id - 𝙎𝙝𝙤𝙬𝙨 𝙄𝘿 𝙤𝙛 𝙖 𝙐𝙨𝙚𝙧 𝙖𝙣𝙙 𝙤𝙛 𝙈𝙚𝙙𝙞𝙖\n➤ /addnote - 𝘼𝙙𝙙 𝙉𝙤𝙩𝙚𝙨 𝙞𝙣 𝙮𝙤𝙪𝙧 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘽𝙤𝙩\n➤ /notes - 𝘾𝙝𝙚𝙘𝙠 𝙖𝙡𝙡 𝙩𝙝𝙚 𝙣𝙤𝙩𝙚𝙨 𝙞𝙣 𝙮𝙤𝙪𝙧 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘽𝙤𝙩\n➤ /rmnote - 𝙍𝙚𝙢𝙤𝙫𝙚 𝙣𝙤𝙩𝙚𝙨 𝙛𝙧𝙤𝙢 𝙮𝙤𝙪𝙧 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘽𝙤𝙩\n➤ /alive - 𝘼𝙢 𝙄 𝘼𝙡𝙞𝙫𝙚 ??\n➤ /ban - 𝘽𝙖𝙣𝙨 𝘼 𝙐𝙨𝙚𝙧 𝙛𝙧𝙤𝙢 𝙩𝙝𝙚 𝘾𝙝𝙖𝙩 {𝙒𝙤𝙧𝙠𝙨 𝙊𝙣𝙡𝙮 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥𝙨}\n➤ /unban - 𝙐𝙣𝘽𝙖𝙣𝙨 𝘼 𝙐𝙨𝙚𝙧 𝙛𝙧𝙤𝙢 𝙩𝙝𝙚 𝘾𝙝𝙖𝙩 {𝙒𝙤𝙧𝙠𝙨 𝙊𝙣𝙡𝙮 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥𝙨}\n➤ /promote - 𝙋𝙧𝙤𝙢𝙤𝙩𝙚𝙨 𝙖 𝙐𝙨𝙚𝙧 𝙞𝙣 𝙩𝙝𝙚 𝘾𝙝𝙖𝙩 {𝙒𝙤𝙧𝙠𝙨 𝙊𝙣𝙡𝙮 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥𝙨}\n➤ /demote - 𝘿𝙚𝙢𝙤𝙩𝙚𝙨 𝙖 𝙐𝙨𝙚𝙧 𝙞𝙣 𝙩𝙝𝙚 𝘾𝙝𝙖𝙩 {𝙒𝙤𝙧𝙠𝙨 𝙊𝙣𝙡𝙮 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥𝙨}\n➤ /pin - 𝙋𝙞𝙣𝙨 𝙖 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙞𝙣 𝙩𝙝𝙚 𝘾𝙝𝙖𝙩 {𝙒𝙤𝙧𝙠𝙨 𝙊𝙣𝙡𝙮 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥𝙨}\n➤ /stats - 𝙎𝙝𝙤𝙬𝙨 𝙩𝙤𝙩𝙖𝙡 𝙐𝙨𝙚𝙧𝙨 𝙞𝙣 𝙮𝙤𝙪𝙧 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘽𝙤𝙩\n➤ /purge - 𝙋𝙪𝙧𝙜𝙚𝙨 𝙖𝙡𝙡 𝙢𝙚𝙨𝙨𝙖𝙜𝙚𝙨, 𝙛𝙧𝙤𝙢 𝙩𝙝𝙚 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙧𝙚𝙥𝙡𝙞𝙚𝙙 {𝙒𝙤𝙧𝙠𝙨 𝙊𝙣𝙡𝙮 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥𝙨, 𝙏𝙝𝙚 𝘽𝙤𝙩 𝙨𝙝𝙤𝙪𝙡𝙙 𝙗𝙚 𝙖𝙣 𝘼𝙙𝙢𝙞𝙣 𝙬𝙞𝙩𝙝 𝘿𝙚𝙡𝙚𝙩𝙚 𝙈𝙚𝙨𝙨𝙖𝙜𝙚𝙨 𝙧𝙞𝙜𝙝𝙩}\n➤ /del - 𝙍𝙚𝙥𝙡𝙮 𝙩𝙤 𝙖 𝙢𝙚𝙨𝙨𝙖𝙜𝙚, 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙙𝙚𝙡𝙚𝙩𝙚 {𝙒𝙤𝙧𝙠𝙨 𝙊𝙣𝙡𝙮 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥𝙨, 𝙏𝙝𝙚 𝘽𝙤𝙩 𝙨𝙝𝙤𝙪𝙡𝙙 𝙗𝙚 𝙖𝙣 𝘼𝙙𝙢𝙞𝙣 𝙬𝙞𝙩𝙝 𝘿𝙚𝙡𝙚𝙩𝙚 𝙈𝙚𝙨𝙨𝙖𝙜𝙚𝙨 𝙧𝙞𝙜𝙝𝙩}"
    await assistant.send_message(event.chat_id, grabon)


# Bot Permit.
@assistant.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    if is_he_added(event.sender_id):
        return
    if event.raw_text.startswith("/"):
        pass
    elif event.sender_id == bot.uid:
        return
    else:
        await event.get_sender()
        event.chat_id
        sed = await event.forward_to(bot.uid)
        # Add User To Database ,Later For Broadcast Purpose
        # (C) @SpecHide
        add_me_in_db(sed.id, event.sender_id, event.id)


@assistant.on(events.NewMessage(func=lambda e: e.is_private))
async def sed(event):
    msg = await event.get_reply_message()
    user_id, reply_message_id = his_userid(msg.id)
    if event.sender_id == bot.uid:
        if event.text.startswith("/"):
            pass
        else:
            await assistant.send_message(user_id, event.message)


# broadcast
@assistant.on(
    events.NewMessage(
        pattern="^/broadcast ?(.*)", func=lambda e: e.sender_id == bot.uid
    )
)
async def sedlyfsir(event):
    msgtobroadcast = event.pattern_match.group(1)
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for starkcast in userstobc:
        try:
            sent_count += 1
            await assistant.send_message(int(starkcast.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except Exception as e:
            try:
                logger.info(f"Error : {error_count}\nError : {e} \nUsers : {chat_id}")
            except:
                pass
    await assistant.send_message(
        event.chat_id,
        f"𝑩𝒓𝒐𝒂𝒅𝑪𝒂𝒔𝒕𝒆𝒅 𝒕𝒉𝒆 𝑮𝒊𝒗𝒆𝒏 𝑴𝒆𝒔𝒔𝒂𝒈𝒆\n\n𝘽𝙧𝙤𝙖𝙙𝘾𝙖𝙨𝙩 𝙘𝙤𝙢𝙥𝙡𝙚𝙩𝙚𝙙 𝙞𝙣 : {sent_count} 𝙂𝙧𝙤𝙪𝙥𝙨/𝙐𝙨𝙚𝙧𝙨\n𝑩𝒓𝒐𝒂𝒅𝑪𝒂𝒔𝒕 𝒈𝒐𝒕 𝑬𝒓𝒓𝒐𝒓 𝒊𝒏 : {error_count} 𝙂𝙧𝙤𝙪𝙥𝙨/𝙐𝙨𝙚𝙧𝙨\n\n𝙏𝙤𝙩𝙖𝙡 𝘾𝙝𝙖𝙩𝙨 (𝙂𝙧𝙤𝙪𝙥𝙨/𝙐𝙨𝙚𝙧𝙨) 𝙬𝙚𝙧𝙚 : {len(userstobc)}",
    )


@assistant.on(
    events.NewMessage(pattern="^/stats ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    starkisnoob = get_all_users()
    await event.reply(
        f"**𝑺𝒕𝒂𝒕𝒔 𝒐𝒇 𝒚𝒐𝒖𝒓 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 𝑩𝒐𝒕** \n𝙏𝙤𝙩𝙖𝙡 𝙐𝙨𝙚𝙧𝙨 𝙞𝙣 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘽𝙤𝙩 »»» {len(starkisnoob)}"
    )


@assistant.on(events.NewMessage(pattern="^/help", func=lambda e: e.sender_id == bot.uid))
async def starkislub(event):
    grabonx = "**Hᴇʏᴀ!! Bᴇʟᴏᴡ ᴀʀᴇ sᴏᴍᴇ ᴏғ Mʏ Cᴏᴍᴍᴀɴᴅs :**\n➤ /start - 𝘾𝙝𝙚𝙘𝙠 𝙞𝙛 𝙄 𝙖𝙢 𝘼𝙡𝙞𝙫𝙚\n➤ /ping - 𝙋𝙤𝙣𝙜 !\n➤ /tr <lang-code> - 𝙏𝙧𝙖𝙣𝙨𝙡𝙖𝙩𝙚 𝙖 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙡𝙖𝙣𝙜𝙪𝙖𝙜𝙚\n➤ /broadcast - 𝙎𝙚𝙣𝙙𝙨 𝙖 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙏𝙤 𝙖𝙡𝙡 𝙐𝙨𝙚𝙧𝙨 𝙄𝙣 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘽𝙤𝙩\n➤ /id - 𝙎𝙝𝙤𝙬𝙨 𝙄𝘿 𝙤𝙛 𝙖 𝙐𝙨𝙚𝙧 𝙖𝙣𝙙 𝙤𝙛 𝙈𝙚𝙙𝙞𝙖\n➤ /addnote - 𝘼𝙙𝙙 𝙉𝙤𝙩𝙚𝙨 𝙞𝙣 𝙮𝙤𝙪𝙧 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘽𝙤𝙩\n➤ /notes - 𝘾𝙝𝙚𝙘𝙠 𝙖𝙡𝙡 𝙩𝙝𝙚 𝙣𝙤𝙩𝙚𝙨 𝙞𝙣 𝙮𝙤𝙪𝙧 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘽𝙤𝙩\n➤ /rmnote - 𝙍𝙚𝙢𝙤𝙫𝙚 𝙣𝙤𝙩𝙚𝙨 𝙛𝙧𝙤𝙢 𝙮𝙤𝙪𝙧 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘽𝙤𝙩\n➤ /alive - 𝘼𝙢 𝙄 𝘼𝙡𝙞𝙫𝙚 ??\n➤ /ban - 𝘽𝙖𝙣𝙨 𝘼 𝙐𝙨𝙚𝙧 𝙛𝙧𝙤𝙢 𝙩𝙝𝙚 𝘾𝙝𝙖𝙩 {𝙒𝙤𝙧𝙠𝙨 𝙊𝙣𝙡𝙮 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥𝙨}\n➤ /unban - 𝙐𝙣𝘽𝙖𝙣𝙨 𝘼 𝙐𝙨𝙚𝙧 𝙛𝙧𝙤𝙢 𝙩𝙝𝙚 𝘾𝙝𝙖𝙩 {𝙒𝙤𝙧𝙠𝙨 𝙊𝙣𝙡𝙮 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥𝙨}\n➤ /promote - 𝙋𝙧𝙤𝙢𝙤𝙩𝙚𝙨 𝙖 𝙐𝙨𝙚𝙧 𝙞𝙣 𝙩𝙝𝙚 𝘾𝙝𝙖𝙩 {𝙒𝙤𝙧𝙠𝙨 𝙊𝙣𝙡𝙮 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥𝙨}\n➤ /demote - 𝘿𝙚𝙢𝙤𝙩𝙚𝙨 𝙖 𝙐𝙨𝙚𝙧 𝙞𝙣 𝙩𝙝𝙚 𝘾𝙝𝙖𝙩 {𝙒𝙤𝙧𝙠𝙨 𝙊𝙣𝙡𝙮 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥𝙨}\n➤ /pin - 𝙋𝙞𝙣𝙨 𝙖 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙞𝙣 𝙩𝙝𝙚 𝘾𝙝𝙖𝙩 {𝙒𝙤𝙧𝙠𝙨 𝙊𝙣𝙡𝙮 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥𝙨}\n➤ /stats - 𝙎𝙝𝙤𝙬𝙨 𝙩𝙤𝙩𝙖𝙡 𝙐𝙨𝙚𝙧𝙨 𝙞𝙣 𝙮𝙤𝙪𝙧 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘽𝙤𝙩"
    await event.reply(grabonx)


@assistant.on(
    events.NewMessage(pattern="^/block ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if is_he_added(user_id):
        await event.reply("𝑻𝒉𝒊𝒔 𝑼𝒔𝒆𝒓 𝒊𝒔 𝑨𝒍𝒓𝒆𝒂𝒅𝒚 𝑩𝒍𝒂𝒄𝒌𝑳𝒊𝒔𝒕𝒆𝒅.")
    elif not is_he_added(user_id):
        add_nibba_in_db(user_id)
        await event.reply("𝑩𝒍𝒂𝒄𝒌𝑳𝒊𝒔𝒕𝒆𝒅 𝒕𝒉𝒊𝒔 𝑫𝒖𝒎𝒃𝒐 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚")
        await assistant.send_message(
            user_id, "𝒀𝒐𝒖 𝒘𝒆𝒓𝒆 𝑩𝒍𝒂𝒄𝒌𝑳𝒊𝒔𝒕𝒆𝒅 𝒃𝒚 𝒎𝒚 𝑴𝒂𝒔𝒕𝒆𝒓, 𝒏𝒅 𝒏𝒐𝒘 𝒚𝒐𝒖 𝒄𝒂𝒏❜𝒕 𝒔𝒆𝒏𝒅 𝑴𝒆𝒔𝒔𝒂𝒈𝒆𝒔 𝒕𝒐 𝑯𝒊𝒎/𝑯𝒆𝒓."
        )


@assistant.on(
    events.NewMessage(pattern="^/unblock ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if not is_he_added(user_id):
        await event.reply("𝑻𝒉𝒆 𝑼𝒔𝒆𝒓 𝒊𝒔𝒏❜𝒕 𝑩𝒍𝒂𝒄𝒌𝑳𝒊𝒔𝒕𝒆𝒅 🤦🚶")
    elif is_he_added(user_id):
        removenibba(user_id)
        await event.reply("𝑼𝒏-𝑩𝒍𝒂𝒄𝒌𝑳𝒊𝒔𝒕𝒆𝒅 𝒕𝒉𝒊𝒔 𝑫𝒖𝒎𝒃𝒐 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚.")
        await assistant.send_message(
            user_id, "𝑪𝒐𝒏𝒈𝒐!! 𝒀𝒐𝒖 𝒘𝒆𝒓𝒆 𝑼𝒏-𝑩𝒍𝒂𝒄𝒌𝑳𝒊𝒔𝒕𝒆𝒅 𝒃𝒚 𝒎𝒚 𝑴𝒂𝒔𝒕𝒆𝒓, 𝒏𝒅 𝒏𝒐𝒘 𝒚𝒐𝒖 𝒄𝒂𝒏 𝒔𝒆𝒏𝒅 𝒎𝒆𝒔𝒔𝒂𝒈𝒆𝒔 𝒕𝒐 𝑯𝒊𝒎/𝑯𝒆𝒓."
        )

# SuperBot
# made for SuperBot 
