from dictionarytyanbot import bot, dp
import requests
from dictionarytyanbot import bot, dp
from bs4 import BeautifulSoup as BS
from io import StringIO
from config import HEADERS

from aiogram.types import Message
from config import admin_id, URL

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Hi, I'm DictionaryTyan and I help you to understand english words")

@dp.message_handler()
async def dict(message:Message):
    text = URL+message.text
    r = requests.get(text, headers=HEADERS)
    html = BS(r.content, 'lxml')
    mess = f"<b>{html.title.text}</b><pre> </pre>"

    for el in html.select('.e1hk9ate4'):
        title = el.select('.e1q3nk1v3')
        for i in title:
            mess += f"{i.text}<pre> </pre>"

    mess += f"More about <i>{text}</i>"
    await message.answer(text=mess)