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
        [KeyboardButton(text="Игра")],
        [KeyboardButton(text="Наши новости")]
    ],
    resize_keyboard=True
)

game_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Камень, ножницы, бумага")],
        [KeyboardButton(text="Рандомайзер")]
    ],
    resize_keyboard=True
)

keyboard_ingame = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Камень")],
        [KeyboardButton(text="Ножницы")],
        [KeyboardButton(text="Бумага")]
    ],
    resize_keyboard=True
)

news_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О нас")],
        [KeyboardButton(text="Адрес")],
        [KeyboardButton(text="Наши курсы")]
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

@dp.message(lambda message: message.text == "Камень, ножницы, бумага")
async def rps(message: types.Message):
    await message.answer("Выберите камень, ножницы или бумагу:", reply_markup=keyboard_ingame)

@dp.message(lambda message: message.text in ["Камень", "Ножницы", "Бумага"])
async def play_rps(message: types.Message):
    user_choice = message.text
    bot_choice = random.choice(["Камень", "Ножницы", "Бумага"])

    result = dirty_keyboard_ingame(user_choice, bot_choice)

    await message.answer(f"Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}\n{result}")

@dp.message(lambda message: message.text == "Рандомайзер")
async def randomizer(message: types.Message):
    result = random.choice(["Вы победили!", "Вы проиграли!", "Ничья"])
    await message.answer(result)

@dp.message(lambda message: message.text == "О нас")
async def about_us(message: types.Message):
    await message.answer("""Международная IT-академия Geeks (Гикс) была основана Fullstack-разработчиком Айдаром Бакировым
                         и Android-разработчиком Нургазы Сулаймановым в 2018 году в Бишкеке с целью дать возможность каждому человеку,
                         даже без опыта в технологиях, гарантированно освоить IT-профессию.""")

@dp.message(lambda message: message.text == "Адрес")
async def address(message: types.Message):
    await message.answer("Наш адрес: Ош ул. Мырзалы Аматова 1Б, БЦ Томирис, цокольный этаж (здание Визион)")

@dp.message(lambda message: message.text == "Наши курсы")
async def courses(message: types.Message):
    await message.answer("САМЫЕ ВОСТРЕБОВАННЫЕ IT-КУРСЫ В КЫРГЫЗСТАНЕ: SMM PRO 1С, программирование, Data science & machine learning, Graphic design and motion,Тестировщик ПОМы постоянно исследуем рынок труда в поиске самых популярных и перспективных IT-направлений")

def dirty_keyboard_ingame(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "Ничья!"
    elif (user_choice == "Камень" and bot_choice == "Ножницы") or \
         (user_choice == "Ножницы" and bot_choice == "Бумага") or \
         (user_choice == "Бумага" and bot_choice == "Камень"):
        return "Вы победили!"
    else:
        return "Вы проиграли!"

async def on_start():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(on_start())
