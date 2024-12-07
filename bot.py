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


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Добро пожаловать! Выберите одну из опций:", reply_markup=start_keyboard)

@dp.message(lambda message: message.text == "Игра")
async def game(message: types.Message):
    await message.answer("Выберите игру:", reply_markup=game_keyboard)

@dp.message(lambda message: message.text == "Наши новости")
async def news(message: types.Message):
    await message.answer("Выберите раздел новостей:", reply_markup=news_keyboard)

@dp.message(lambda message: message.text == "Камен, ножницы, бумага")
async def rps(message: types.Message):
    await message.answer("Выберите камень, ножницы или бумагу:", reply_markup=keyboard_ingame)

@dp.message(lambda message: message.text in ["Камень", "Ножницы", "Бумага"])
async def play_rps(message: types.Message):
    user_choice = message.text
    bot_choice = random.choice(["Камень", "Ножницы", "Бумага"])

    result = determine_keyboard_ingame(user_choice, bot_choice)

    await message.answer(f"Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}\n{result}")

@dp.message(lambda message: message.text == "Рандомайзер")
async def randomizer(message: types.Message):
    result = random.choice(["Вы победили!", "Вы проиграли!", "Ничья"])
    await message.answer(result)

async def on_start():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(on_start())
