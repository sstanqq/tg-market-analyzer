'''
File for mutually import
'''

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from config import TOKEN

# Initialize bot and dispatcher
bot = Bot(token = TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
