import asyncio
import logging
import sys
import os
import wikipedia
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message


load_dotenv()
TOKEN = os.getenv("API")
dp = Dispatcher()
print("TOKEN:", TOKEN)
wikipedia.set_lang("uz")

@dp.message(Command(commands=["start"]))
async def start_handler(message: Message):
    await message.answer(f"Hello , {html.bold(message.from_user.full_name)}!")


@dp.message()
async def message_handler(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        full =wikipedia.summary(message.text)
        await message.answer(full)
    except:
        await message.answer("Bu mavzu yo`q❌, boshqa yozing❗")


async def main():
    bot = Bot(token=TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML),)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,stream=sys.stdout,)
    asyncio.run(main())
