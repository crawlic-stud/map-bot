from typing import Any

from pydantic import BaseModel
from pymongo.collection import Collection
from aiogram import Bot
from aiogram.types import MenuButtonWebApp, WebAppInfo

from config import locations_db, MAPS_BASE_URL, MAPS_BUTTON_NAME


def convert_dicts_to_type(lst: list[dict[str, Any]], t: BaseModel):
    return [t(**item) for item in lst]


async def db_get_all(db: Collection, _filter: dict[str, Any]):
    everything = db.find(_filter)
    result = []
    async for item in everything:
        result.append(item)
    return result


async def set_users_menu_button(bot: Bot):
    all_users = await locations_db.distinct("user_id")
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text=MAPS_BUTTON_NAME,
            web_app=WebAppInfo(url=f"{MAPS_BASE_URL}/0")
        ))
    for user_id in all_users:
        await bot.set_chat_menu_button(
            chat_id=user_id,
            menu_button=MenuButtonWebApp(
                text=MAPS_BUTTON_NAME,
                web_app=WebAppInfo(url=f"{MAPS_BASE_URL}/{user_id}")
            )
        )
