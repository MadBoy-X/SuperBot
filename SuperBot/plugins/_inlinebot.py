import io
import json
import math
import os
import re
import time
import sys

from telethon import Button, custom, events, functions, version

from SuperBot import CMD_LIST
from SuperBot import ALIVE_NAME
from SuperBot.utils import admin_cmd, sudo_cmd
from platform import uname

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Sᥙρҽɾẞσ𝜏"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)

global ghanti
ghanti = borg.uid
#@command(pattern="^.help ?(.*)")

@borg.on(admin_cmd(pattern=r"ihelp ?(.*)", outgoing=True))
@borg.on(sudo_cmd(pattern=r"ihelp ?(.*)", outgoing=True, allow_sudo=True))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/" , "#", "-", "_", "@"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        global ghanti
        ghanti = borg.uid
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":

            string = ""

            for i in CMD_LIST:

                string += "â¡ï¸" + i + "\n"

                for iter_list in CMD_LIST[i]:

                    string += "    " + str(iter_list) + ""

                    string += "\n"

                string += "\n"

            if len(string) > 69:

                with io.BytesIO(str.encode(string)) as out_file:

                    out_file.name = "cmd.txt"

                    await bot.send_file(

                        event.chat_id,

                        out_file,

                        force_document=True,

                        allow_cache=False,

                        caption="¢σммαη∂ѕ ιη Sᥙρҽɾẞσ𝜏",

                        reply_to=reply_to_id

                    )

                    await event.delete()

            else:

                await event.edit(string)

        elif input_str:

            if input_str in CMD_LIST:

                string = "Cᴏᴍᴍᴀɴᴅ ғᴏᴜɴᴅ ɪɴ {}:\n".format(input_str)

                for i in CMD_LIST[input_str]:

                    string += "  " + i

                    string += "\n"

                await event.edit(string)

            else:

                await event.edit(input_str + " Isɴ'ᴛ A Vᴀʟɪᴅ Pʟᴜɢɪɴ")

        else:

            help_string = f""" 𝙎𝙪𝙥𝙚𝙧𝘽𝙤𝙩 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪\n𝑃𝑟𝑜𝑣𝑖𝑑𝑒𝑑 𝑏𝑦 [{DEFAULTUSER}](tg://user?id={ghanti})\n
𝑫𝒐 `.help` PLUGIN_NAME, 𝑭𝒐𝒓 𝒈𝒆𝒕𝒕𝒊𝒏𝒈 𝑷𝒍𝒖𝒈𝒊𝒏 𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔, 𝒊𝒏 𝒄𝒂𝒔𝒆 𝒕𝒉𝒆 𝒊𝒏𝒍𝒊𝒏𝒆 𝒑𝒐𝒑-𝒖𝒑 𝒅𝒐𝒆𝒔𝒏❜𝒕 𝒘𝒐𝒓𝒌𝒔."""

            results = await bot.inline_query(  # pylint:disable=E0602

                tgbotusername,

                help_string

            )

            await results[0].click(

                event.chat_id,

                reply_to=event.reply_to_msg_id,

                hide_via=True

            )

            await event.delete()

            

@borg.on(admin_cmd(pattern="superbot"))  # pylint:disable=E0602

async def _(event):

    if event.fwd_from:

        return

    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602

    await event.edit(result.stringify())





@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602

async def _(event):

    if event.fwd_from:

        return

    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602

    result = result.stringify()

    logger.info(result)  # pylint:disable=E0602

    await event.edit(f"𝑨𝒏 𝒂𝒅𝒗𝒂𝒏𝒄𝒆𝒅 𝒂𝒏𝒅 𝒎𝒐𝒅𝒊𝒇𝒊𝒆𝒅 𝑼𝒔𝒆𝒓𝑩𝒐𝒕 𝒃𝒂𝒔𝒆𝒅 𝒐𝒏 𝑳𝒂𝒕𝒆𝒔𝒕 [𝑻𝒆𝒍𝒆𝒕𝒉𝒐𝒏](https://pypi.org/project/Telethon/) & [𝑷𝒚𝒕𝒉𝒐𝒏](https://www.python.org/downloads/release/python-390/) 𝑽𝒆𝒓𝒔𝒊𝒐𝒏, 𝑷𝒓𝒐𝒗𝒊𝒅𝒆𝒅 𝒃𝒚 [𝑻𝒆𝒂𝒎 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕](https://github.com/MadBoy-X/SuperBot)")





@borg.on(admin_cmd(pattern="syntax (.*)"))

async def _(event):

    if event.fwd_from:

        return

    plugin_name = event.pattern_match.group(1)



    if plugin_name in CMD_LIST:

        help_string = CMD_LIST[plugin_name].doc

        unload_string = f"𝙐𝙨𝙚 `.unload` {plugin_name} 𝙏𝙤 𝙧𝙚𝙢𝙤𝙫𝙚 𝙩𝙝𝙞𝙨 𝙋𝙡𝙪𝙜𝙞𝙣.\n           Â © Sᥙρҽɾẞσ𝜏"

        

        if help_string:

            plugin_syntax = f"𝙎𝙮𝙣𝙩𝙖𝙭 𝙛𝙤𝙧 𝙋𝙡𝙪𝙜𝙞𝙣 {plugin_name}:\n\n{help_string}\n{unload_string}"

        else:

            plugin_syntax = f"𝙉𝙤 `DOCSTRING` 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙨𝙚𝙩𝙪𝙥 𝙛𝙤𝙧 {plugin_name} 𝙋𝙡𝙪𝙜𝙞𝙣."

    else:



        plugin_syntax = "𝙀𝙣𝙩𝙚𝙧 𝙖 𝙫𝙖𝙡𝙞𝙙 𝙋𝙡𝙪𝙜𝙞𝙣 𝙉𝙖𝙢𝙚.\n𝘿𝙤 `.plinfo` 𝙤𝙧 `.help` 𝙩𝙤 𝙜𝙚𝙩 𝙩𝙝𝙚 𝙡𝙞𝙨𝙩 𝙤𝙛 𝙫𝙖𝙡𝙞𝙙 𝙋𝙡𝙪𝙜𝙞𝙣 𝙉𝙖𝙢𝙚𝙨."



    await event.edit(plugin_syntax)
