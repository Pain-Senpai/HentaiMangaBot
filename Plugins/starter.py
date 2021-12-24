from Helper.helper import start_text, help_text
from config import bot
from telethon import events
class start():
    @bot.on(events.NewMessage(pattern="/start"))
    async def event_handler_start(event):
        await bot.send_message(
            event.chat_id,
            start_text,
            file='https://telegra.ph/file/c1c7cd4675c459244469a.mp4'
        )

    @bot.on(events.NewMessage(pattern="/help"))
    async def event_handler_help(event):
        await bot.send_message(
            event.chat_id,
            help_text
            )

    @bot.on(events.NewMessage(pattern="/source"))
    async def event_handler_source(event):
        await bot.send_message(
            event.chat_id,
            '[Project Tsukiyomi](https://t.me/Project_Tsukiyomi/6)\n Provides you some doujins ofcourse the source code is private'
        )
