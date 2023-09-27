import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.chat_action import ChatActionMiddleware


# import bot_text

# BOT_TOKEN = '6634594271:AAH6xlwrTztXgkz1iNHgdZW7JeFPz65PTrI'
# router = Router()

# async def main():
#     bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
#     dp = Dispatcher(storage=MemoryStorage())
#     dp.include_router(router)
#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


# # @router.message(Command("start"))
# # async def start_handler(msg: Message):
# #     await msg.answer("Hi! I am here to tell you all about cool events in Tel-Aviv!")


# # @router.message()
# # async def message_handler(msg: Message):
# #     await msg.answer(f"Your ID: {msg.from_user.id}")

# #Create Buttons

# menu = [
#     [InlineKeyboardButton(text="💎 Events for today"), #callback_data="generate_text",
#     InlineKeyboardButton(text="🎁 Events for next 7 days")]
# ]
# menu = InlineKeyboardMarkup(inline_keyboard=menu)
# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Go back to the menu")]], resize_keyboard=True)
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Go back to the menu")]])
 
# greet = "Hi, {name}, I am here to tell you all about cool events in Tel-Aviv"
# menu = "📍 Menu"
# err = "🚫 There is an error, please try later"

# @router.message(Command("start"))
# async def start_handler(msg: Message):
#     await msg.answer(greet.format(name=msg.from_user.full_name), reply_markup=menu)

# @router.message(F.text == "Menu")
# @router.message(F.text == "Go back to the menu")
# @router.message(F.text == "◀️ Go back to the menu")
# async def menu(msg: Message):
#     await msg.answer(menu, reply_markup=menu)


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     # message.middleware(ChatActionMiddleware())
#     asyncio.run(main())
