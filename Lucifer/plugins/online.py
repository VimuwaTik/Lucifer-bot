# Copyright Lucifer
# For @LuciferHelp coded by @xditya
# Kangers keep credits else I'll take down š§

import random
import sys

from telethon import version

from Lucifer import ALIVE_NAME
from Lucifer.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lucifer User"

ONLINESTR = [
    "āāāāāāāāāāāāāāāāāāāā \nāāā¦āā¦āāā¦āāāāāāā¦āāāāā  āāāāāā āāāāāāāāāāā āāā \nāāāā©āāāāāāāāāā©āā©āāāā \nāāāāāāāāāāāāāāāāāāāā \n\n**Lucifer  online.**\n\n**All systems functioning normally !** \n\n**Bot by** [Team Lucifer](tg://user?id=804329190) \n\n**More help -** @LuciferXUpdates \n\n           [š§ GitHub Repository š§](https://github.com/kaal0408/Lucifer-X)",
    f"ā¦āā¦āāā¦āāāāāāā¦āāā\nāāāā āāāāāāāāāāā ā\nāā©āāāāāāāāāā©āā©āā\n              **Welcome to Lucifer**\n\n**Hey master! I'm alive. All systems online and functioning normally ā**\n\n**āļø Telethon version:** `{version.__version__}` \n\n**āļø Python:** `{sys.version}` \n\nāļø More info: @LuciferXUpdates \n\nāļø Created by: [Team Lucifer](tg://user?id804329190=) \n\n**āļø Database status:** All ok š \n\n**āļø My master:** {DEFAULTUSER} \n\n        [š Github repository š](https://github.com/kaal0408/Lucifer-X)",
]


@Lucifer.on(admin_cmd(outgoing=True, pattern="online"))
@Lucifer.on(sudo_cmd(allow_sudo=True, pattern="online"))
async def online(event):
    """Greet everyone!"""
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await eor(event, random.choice(ONLINESTR))
