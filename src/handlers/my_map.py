from aiogram import types
from aiogram.filters import Command

from config import dp, MAPS_BASE_URL


@dp.message(Command("map"))
async def get_my_map(m: types.Message):
    my_map = f"{MAPS_BASE_URL}/{m.from_user.id}"
    btn = types.InlineKeyboardButton(text=f"Карта @{m.from_user.username}", url=my_map)
    await m.answer(
        f"Ссылка на твои <a href='{my_map}'>места</a> 👇",
        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[btn]]),
    )
