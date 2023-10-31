from aiogram import types
from aiogram.filters import Command
from aiogram.types import MenuButtonWebApp, WebAppInfo

from config import dp, bot, MAPS_BASE_URL, MAPS_BUTTON_NAME
from .save_location import location_kb


START_MSG = """

"""


@dp.message(Command("start", "help"))
async def cmd_start(message: types.Message):
    await bot.set_chat_menu_button(
        chat_id=message.from_user.id,
        menu_button=MenuButtonWebApp(
            text=MAPS_BUTTON_NAME,
            web_app=WebAppInfo(url=f"{MAPS_BASE_URL}/{message.from_user.id}"),
        ),
    )
    await message.answer(
        (
            f"Привет, {message.from_user.first_name}!\n"
            "Я помогу тебе запомнить твои любимые места и больше никогда их не терять 🥳\n\n"
            "<b>Простая инструкция:</b>\n"
            '1) Жми на кнопку "Сохранить место" или отправь мне любую геолокацию\n'
            "2) Вводи название нового места\n"
            "3) Просматривай свою карту по кнопке слева внизу 😉\n\n"
            '<span class="tg-spoiler"><i> * Также, при помощи команды /map ты можешь поделиться своей картой с друзьями</i></span>'
        ),
        reply_markup=location_kb,
    )
    await message.answer("👇")
    # await message.answer(" 😉")
