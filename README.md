# SᴜᴘᴇʀBᴏᴛ

A modified and advanced UserBot for Telegram Users. Based on Latest Telethon (1.21.1) and made using Latest Python (3.9.5). **Managed By : [@its_JassManak](https://telegram.me/its_JassManak). DEVs : [@Disheartened_007](https://telegram.me/Disheartened_007), [@ItS_PRaNAv_Xd](https://telegram.me/ItS_PRaNAv_Xd).**

-------------------------------------------------

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f7c51539e67b483bb8d7749acca51d3a)](https://app.codacy.com/gh/MadBoy-X/SuperBot?utm_source=github.com&utm_medium=referral&utm_content=MadBoy-X/SuperBot&utm_campaign=Badge_Grade_Settings)

![GitHub repo size](https://img.shields.io/github/repo-size/MadBoy-X/SuperBot)

-------------------------------------------------

# Dᴇᴘʟᴏʏ:-

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FMadBoy-X%2FSuperBot-Deploy&template=https%3A%2F%2Fgithub.com%2FMadBoy-X%2FSuperBot-Deploy)

------------------------------------------------

# Sᴛʀɪɴɢ Sᴇssɪᴏɴ:-

## [String Session](https://replit.com/@madboy482/SuperBot)

-------------------------------------------------

## The owner/devs won't be responsible for any kind of bans due to the bot...
## Fᴏʀᴋ Aᴛ Yᴏᴜʀ Oᴡɴ Rɪsᴋ

-------------------------------------------------

## Iɴsᴛᴀʟʟɪɴɢ (Nᴏʀᴍᴀʟ Wᴀʏ)

Simply clone the repository and run the main file:
```sh
git clone https://github.com/MadBoy-X/SuperBot
cd SuperBot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m SuperBot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### Uɴɪʙᴏʀɢ Cᴏɴғɪɢʀɪᴜᴛɪᴏɴ

The UniBorg Config is situated in `SuperBot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
UnFortunately, there are no Mandatory vars for the UniBorg Support Config.

## Mᴀɴᴅᴀᴛᴏʀʏ Vᴀʀs

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org 
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The SuperBot will not work without setting the mandatory vars.

-------------------------------------------------

# Cʀᴇᴅɪᴛs 📍
## • MADBOY   »»  <a href="https://github.com/madboy482" alt="MadBoy"> <img src="https://img.shields.io/badge/MadBoy-30302f?logo=github" /></a>
## • JASS MANAK  »»  <a href="https://github.com/JassManak1125" alt="Jass Manak"> <img src="https://img.shields.io/badge/Jass Manak-98AFC7?logo=github" /></a>
## • PRANAV  »»  <a href="https://github.com/Pranav18262" alt="Pranav"> <img src="https://img.shields.io/badge/Pranav-625D5D?logo=github" /></a>
## • SHUBHANSH »» <a href="https://github.com/Aruoto" alt="Shubhansh"> <img src="https://img.shields.io/badge/Shubhansh-E5E4E2?logo=github" /></a>

-------------------------------------------------

# Licence 📋
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

## Copyright (C) 2021 by Team SuperBot for SuperBot UserBot, < https://github.com/MadBoy-X >.

