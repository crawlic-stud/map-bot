from typing import Any
from pymongo.collection import Collection
from pydantic import BaseModel


def convert_dicts_to_type(lst: list[dict[str, Any]], t: BaseModel):
    return [t(**item) for item in lst]


async def db_get_all(db: Collection, _filter: dict[str, Any]):
    everything = db.find(_filter)
    result = []
    async for item in everything:
        result.append(item)
    return result
