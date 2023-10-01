from aiogram import types
from aiogram.filters import Command

from config import dp
from .save_location import location_kb


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!", reply_markup=location_kb)
