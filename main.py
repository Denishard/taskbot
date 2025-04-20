import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: Message):
    await message.answer("Привет! Я твой помощник по задачам. Напиши задачу или запиши голосовое сообщение!")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    executor.start_polling(dp)
