from aiogram import Bot, types, Dispatcher

from data import config

# Создаем переменную бота
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# Создаем диспетчер
dp = Dispatcher(bot)