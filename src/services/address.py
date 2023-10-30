from typing import NamedTuple

import aiohttp


URL = "https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1"


class Address(NamedTuple):
    city: str | None
    country: str | None
    street: str | None
    house_number: str | None


async def get_address(lat: float, lon: float) -> Address:
    url = URL.format(lat=lat, lon=lon)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            address_data = data.get("address", {})
            return Address(
                city=address_data.get("city"),
                country=address_data.get("country"),
                street=address_data.get("road"),
                house_number=address_data.get("house_number"),
            )


def format_address(address: Address) -> str:
    return ", ".join([value for value in address if value is not None])
