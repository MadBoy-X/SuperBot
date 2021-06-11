#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""𝙋𝙡𝙚𝙖𝙨𝙚 𝙜𝙤 𝙩𝙤 my.telegram.org
𝙇𝙤𝙜𝙞𝙣 𝙪𝙨𝙞𝙣𝙜 𝙮𝙤𝙪𝙧 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙖𝙘𝙘𝙤𝙪𝙣𝙩
𝘾𝙡𝙞𝙘𝙠 𝙤𝙣 𝘼𝙋𝙄 𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙢𝙚𝙣𝙩 𝙏𝙤𝙤𝙡𝙨
𝘾𝙧𝙚𝙖𝙩𝙚 𝙖 𝙣𝙚𝙬 𝙖𝙥𝙥𝙡𝙞𝙘𝙖𝙩𝙞𝙤𝙣, 𝙗𝙮 𝙚𝙣𝙩𝙚𝙧𝙞𝙣𝙜 𝙩𝙝𝙚 𝙧𝙚𝙦𝙪𝙞𝙧𝙚𝙙 𝙙𝙚𝙩𝙖𝙞𝙡𝙨, 𝒂𝒏𝒅 𝒕𝒉𝒆𝒏 𝒆𝒏𝒕𝒆𝒓 𝒕𝒉𝒆 𝑨𝑷𝑷_𝑰𝑫 𝒂𝒏𝒅 𝑨𝑷𝑰_𝑯𝑨𝑺𝑯 𝒃𝒆𝒍𝒐𝒘 :""")
APP_ID = int(input("𝑬𝒏𝒕𝒆𝒓 𝑨𝑷𝑷 𝑰𝑫 𝒉𝒆𝒓𝒆 : "))
API_HASH = input("𝑬𝒏𝒕𝒆𝒓 𝑨𝑷𝑰 𝑯𝑨𝑺𝑯 𝒉𝒆𝒓𝒆 : ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
