import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as x
from telethon import __version__ as y
from pyrogram import __version__ as z
from Messi.events import register
from Messi import telethn as tbot


PHOTO = "https://graph.org//file/97d0300235de510b0f586.mp4"

@register(pattern=("Awake Johan"))
@register(pattern=("Awake johan"))
@register(pattern=("Awake Liebert"))
@register(pattern=("Awake liebert"))
@register(pattern=("awake Johan"))
@register(pattern=("awake johan"))
@register(pattern=("awake liebert"))
@register(pattern=("awake liebert"))
@register(pattern=("awake libert"))
@register(pattern=("Awake libert"))
@register(pattern=("Awake johan libert"))
@register(pattern=("/awake"))
@register(pattern=("/Awake"))
@register(pattern=("/alive"))
@register(pattern=("/Alive"))
@register(pattern=("/wake"))
@register(pattern=("/wakeup"))          
          


async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Johan Liebert** \n\n"
  TEXT += "🗿 **I'm Working Properly** \n\n"
  TEXT += f"🗿 **My Developers : [Johan Creators](https://t.me/shoushuke_updates/3)** \n\n"
  TEXT += f"🗿 **Library Version :** `{x}` \n\n"
  TEXT += f"🗿 **Telethon Version :** `{y}` \n\n"
  TEXT += f"🗿 **Pyrogram Version :** `{z}` \n\n"
  TEXT += "**🗿 Thanks For Adding Me Here **"
  BUTTON = [[Button.url("Help", "https://t.me/johan_liebert_probot?start=help"), Button.url("My Headquarters", "https://t.me/shoushuke_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
