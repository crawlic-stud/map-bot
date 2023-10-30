import asyncio


async def main():
    module = __import__("database.migrations").migrations
    vars = dir(module)
    migrations = [var for var in vars if var.startswith("m_")]
    for migration in migrations:
        async_func = getattr(module, migration)
        await async_func()
    return


if __name__ == "__main__":
    asyncio.run(main())
