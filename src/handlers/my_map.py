from aiogram import types
from aiogram.filters import Command

from config import dp, locations_db
from models import LocationInDb
from services import map_display
import utils


@dp.message(Command("map"))
async def get_my_map(m: types.Message):
    raw_locs = await utils.db_get_all(locations_db, {"user_id": m.from_user.id})
    locs: list[LocationInDb] = utils.convert_dicts_to_type(
        raw_locs, LocationInDb)
    map_bytes = map_display.get_map_bytes(locs)
    f = types.BufferedInputFile(map_bytes, filename=f"{m.from_user.username}_map.html")
    await m.answer_document(f, caption="Твоя карта!")
    