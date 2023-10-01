import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from pymongo.collection import Collection
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI


load_dotenv()
TOKEN = os.getenv("TG_TOKEN")
MONGO_USER = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_HOST = os.getenv("MONGO_HOST")

MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
DB_NAME = "locbot"

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()
logger = logging.getLogger("bot")

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongo_client.get_io_loop = asyncio.get_running_loop
db: Collection = mongo_client[DB_NAME]

locations_db = db["locations"]

app = FastAPI()
API_HOST = os.getenv("UVICORN_HOST")
API_PORT = int(os.getenv("API_PORT"))
MAPS_URL = os.getenv("MAPS_URL")
