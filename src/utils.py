from typing import Any

from pydantic import BaseModel
from pymongo.collection import Collection
from aiogram import Bot
from aiogram.types import MenuButtonWebApp, WebAppInfo

from config import locations_db


def convert_dicts_to_type(lst: list[dict[str, Any]], t: BaseModel):
    return [t(**item) for item in lst]


async def db_get_all(db: Collection, _filter: dict[str, Any]):
    everything = db.find(_filter)
    result = []
    async for item in everything:
        result.append(item)
    return result


async def set_users_menu_button(bot: Bot, btn_name: str, base_url: str):
    all_users = await locations_db.distinct("user_id")
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text=btn_name,
            web_app=WebAppInfo(url=f"{base_url}/0")
        ))
    for user_id in all_users:
        await bot.set_chat_menu_button(
            chat_id=user_id,
            menu_button=MenuButtonWebApp(
                text=btn_name,
                web_app=WebAppInfo(url=f"{base_url}/{user_id}")
            )
        )
