import asyncio

from config import locations_db
from services.address import get_address, format_address


async def m_add_addresses():
    all_locations = locations_db.find()
    async for loc in all_locations:
        if not loc.get("address"):
            address = await get_address(loc["latitude"], loc["longitude"])
            asyncio.sleep(0.05)
            await locations_db.update_one(
                {"_id": loc["_id"]}, {"$set": {"address": format_address(address)}}
            )
