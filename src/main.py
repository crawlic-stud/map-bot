import logging
import asyncio

from config import dp, bot, MAPS_URL
import handlers
import utils


async def main():
    await utils.set_users_menu_button(
        bot=bot, 
        btn_name="Моя карта 🗺", 
        base_url=f"{MAPS_URL}/map")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
