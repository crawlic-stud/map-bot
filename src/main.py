import logging
import asyncio

from aiogram.types import BotCommand

from config import dp, bot
import handlers
import utils


async def main():
    await bot.set_my_commands([
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="map", description="Поделиться картой"),
    ])
    await utils.set_users_menu_button(bot=bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
