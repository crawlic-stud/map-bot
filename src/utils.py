import base64
from pathlib import Path
from typing import Any
import urllib.parse

from pydantic import BaseModel
from pymongo.collection import Collection
from aiogram import Bot
from aiogram.types import MenuButtonWebApp, WebAppInfo

from config import locations_db, logger, MAPS_BASE_URL, MAPS_BUTTON_NAME
from models import IconInfo


DEFAULT_COLOR1 = "4dffd5"
DEFAULT_COLOR2 = "154515"


def convert_dicts_to_type(lst: list[dict[str, Any]], t: BaseModel):
    return [t(**item) for item in lst]


async def db_get_all(db: Collection, _filter: dict[str, Any]):
    everything = db.find(_filter)
    result = []
    async for item in everything:
        result.append(item)
    return result


async def set_menu_button(bot: Bot, user_id: int | None = None):
    await bot.set_chat_menu_button(
        chat_id=user_id,
        menu_button=MenuButtonWebApp(
            text=MAPS_BUTTON_NAME, web_app=WebAppInfo(url=f"{MAPS_BASE_URL}/{user_id}")
        ),
    )


async def set_users_menu_button(bot: Bot):
    all_users = await locations_db.distinct("user_id")
    await set_menu_button(bot)
    for user_id in all_users:
        try:
            await set_menu_button(bot, user_id)
        except Exception as e:
            logger.error(f"Error with user {user_id}: {e}")


def replace_default_colors(svg: str) -> str:
    svg = svg.replace(DEFAULT_COLOR1, "color1")
    svg = svg.replace(DEFAULT_COLOR2, "color2")
    return svg


def get_all_icons() -> list[IconInfo]:
    icons_path = Path.cwd() / "src/static/icons"
    result = []
    for icon in icons_path.glob("*.svg"):
        path = icon.name
        svg = icon.read_text()
        # svg = replace_default_colors(svg)
        svg_uri = urllib.parse.quote(svg, safe=":/?=")
        data_uri = f"data:image/svg+xml,{svg_uri}"
        result.append(
            IconInfo(name=path.replace(".svg", ""), path=path, content=data_uri)
        )
    return result
