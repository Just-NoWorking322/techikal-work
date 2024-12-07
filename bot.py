import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio
import logging

from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Игра")],
        [KeyboardButton("Наши новости")]
    ],
    resize_keyboard=True
)

game_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Камен, ножницы, бумага")],
        [KeyboardButton("Рандомайзер")]
    ],
    resize_keyboard=True
)

keyboard_ingame = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Камень")],
        [KeyboardButton("Ножницы")],
        [KeyboardButton("Бумага")]
    ],
    resize_keyboard=True
)

news_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("О нас")],
        [KeyboardButton("Адрес")],
        [KeyboardButton("Наши курсы")]
    ],
    resize_keyboard=True
)

async def on_start():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(on_start())
