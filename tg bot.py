import os
import psycopg2
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from data import Database
load_dotenv()
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton




API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    frist_name = message.from_user.first_name
    user_id = message.from_user.id
    query=f"insert into data_tg(frist_name,user_id) values('{frist_name}',{user_id})"
    await message.answer("Assalomu alaykum!", reply_markup=create_default_keyboard())


def create_default_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Menyu 1"), KeyboardButton("Menyu 2"), KeyboardButton("Menyu 3"))
    keyboard.add(KeyboardButton("Menyu 4"), KeyboardButton("Menyu 5"), KeyboardButton("Menyu 6"))
    keyboard.add(KeyboardButton("Menyu 7"))
    keyboard.add(KeyboardButton("Menyu 8"))
    return keyboard


def create_inline_keyboard():
    inline_keyboard = InlineKeyboardMarkup()
    inline_keyboard.add(
        InlineKeyboardButton(text="➖", callback_data="minus"),
        InlineKeyboardButton(text="Count", callback_data="count"),
        InlineKeyboardButton(text="➕", callback_data="plus")
    )
    return inline_keyboard



@dp.message_handler(lambda message: message.text.startswith('Menyu'))
async def button_click(message: types.Message):
    await message.answer("Default keyboard", reply_markup=create_default_keyboard())
    await message.answer("Inline keyboard:", reply_markup=create_inline_keyboard())


class Counter:
    minus_count = 0
    plus_count = 0


@dp.callback_query_handler(lambda c: c.data)
async def inline_button_click(callback_query: types.CallbackQuery):
    code = callback_query.data
    await bot.answer_callback_query(callback_query.id)

    if code == "minus":
        Counter.minus_count += 1
        await bot.send_message(callback_query.from_user.id, "Minus ")
    elif code == "count":
        await bot.send_message(callback_query.from_user.id, f"Count: Minus {Counter.minus_count}, Plus {Counter.plus_count} ")
    elif code == "plus":
        Counter.plus_count += 1
        await bot.send_message(callback_query.from_user.id, "Plus ")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)