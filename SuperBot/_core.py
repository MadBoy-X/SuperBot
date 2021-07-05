# SuperBot
# made for SuperBot

import asyncio
import os
from datetime import datetime
from pathlib import Path

from SuperBot import ALIVE_NAME
from SuperBot import bot 
from SuperBot.utils import admin_cmd, load_module, remove_plugin, sudo_cmd
from SuperBot.utils import edit_or_reply as eor

DELETE_TIMEOUT = 3
thumb_image_path = "./Resources/SuperBot4.jpg"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Sᥙρҽɾẞσ𝜏"


@bot.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    message_id = event.message.id
    thumb = thumb_image_path
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./SuperBot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await eor(
            pro,
            f"**»»» 𝙋𝙡𝙪𝙜𝙞𝙣 𝙉𝙖𝙢𝙚 :** `{input_str}`\n**»»» 𝙐𝙥𝙡𝙤𝙖𝙙𝙚𝙙 𝙄𝙣 :** `{time_taken_in_ms} 𝑺𝒆𝒄𝒐𝒏𝒅𝒔`.\n**»»» 𝙐𝙥𝙡𝙤𝙖𝙙𝙚𝙙 𝘽𝙮 :** `{DEFAULTUSER}`\n",
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.edit("𝐒𝐞𝐧𝐭 ❗❗❗") # only italic if loaded markdown else it doesn't look grp
    else:
        await eor(event, "**Sσɾɾყ :** 𝑭𝒊𝒍𝒆 𝒏𝒐𝒕 𝑭𝒐𝒖𝒏𝒅")


@bot.on(admin_cmd(pattern="install -true"))
@bot.on(sudo_cmd(pattern="install -true", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "SuperBot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await eor(
                    event,
                    "𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚 𝑰𝒎𝒑𝒐𝒓𝒕𝒆𝒅 {}".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                await eor(
                    event,
                    "**Ɛɾɾσɾ ❗❗**\n\n𝑷𝒍𝒖𝒈𝒊𝒏 𝒄𝒂𝒏𝒏𝒐𝒕 𝒃𝒆 𝒊𝒎𝒑𝒐𝒓𝒕𝒆𝒅❗\n𝑴𝒊𝒈𝒉𝒕 𝒉𝒂𝒗𝒆 𝒃𝒆𝒆𝒏 𝒊𝒎𝒑𝒐𝒓𝒕𝒆𝒅 𝒑𝒓𝒆𝒗𝒊𝒐𝒖𝒔𝒍𝒚.",
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await eor(event, str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@bot.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
@bot.on(sudo_cmd(pattern=r"unload (?P<shortname>\w+)$", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        qwe = await eor(event, f"{shortname} 𝑼𝒏𝒍𝒐𝒂𝒅𝒆𝒅 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚  𝒃𝒚 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕.")
    except Exception as e:
        await qwe.edit(
            "{shortname} 𝑼𝒏𝒍𝒐𝒂𝒅𝒆𝒅 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚 𝒃𝒚 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕.\n{}".format(shortname, str(e))
        )


@bot.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
@bot.on(sudo_cmd(pattern=r"load (?P<shortname>\w+)$", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        qwe = await eor(event, f"{shortname} 𝑳𝒐𝒂𝒅𝒆𝒅 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚 𝒃𝒚 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕.")
    except Exception as e:
        await qwe.edit(
            f"{shortname} 𝒄𝒂𝒏❜𝒕 𝒃𝒆 𝒍𝒐𝒂𝒅𝒆𝒅 𝒃𝒚 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕\n𝑪𝒖𝒛 𝒐𝒇 𝒂𝒏 𝑬𝒓𝒓𝒐𝒓\n\n{str(e)}"
        )

# SuperBot
# made for SuperBot
