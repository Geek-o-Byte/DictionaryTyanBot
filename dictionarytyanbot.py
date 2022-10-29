import asyncio

from aiogram import Bot, Dispatcher, executor, types
import config
import logging

loop = asyncio.get_event_loop()

bot = Bot(token=config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)