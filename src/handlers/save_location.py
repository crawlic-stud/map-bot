from aiogram import types, F 
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from config import dp, locations_db
from models import LocationInDb
from .cancel_state import cancel_button


SAVE_TEXT = "Сохранить место ❤️" 
location_kb = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text=SAVE_TEXT, request_location=True)]
    ],
    resize_keyboard=True,
    is_persistent=True
)


class SaveLocation(StatesGroup):
    enter_name = State()


@dp.message(F.location)
async def save_location(m: types.Message, state: FSMContext):
    loc = m.location
    
    res = await locations_db.insert_one(
        LocationInDb(
            latitude=loc.latitude,
            longitude=loc.longitude,
            name="Без названия",
            user_id=m.from_user.id
        ).dict()
    )
    loc_id = res.inserted_id
    await m.answer(
        "Как хочешь назвать это место? ✨",
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[[cancel_button]]
    ))    
    await state.set_state(SaveLocation.enter_name)
    await state.set_data({"loc_id": loc_id})
    
    
@dp.message(SaveLocation.enter_name)
async def save_name(m: types.Message, state: FSMContext):
    data = await state.get_data()
    loc_id = data["loc_id"]
    
    res = await locations_db.update_one(
        {"_id": loc_id},
        {"$set": {
            "name": m.text
        }}
    )
    if res.modified_count:
        await m.answer(f"Сохранил с именем: <b>{m.text}</b>")
    else:
        await m.answer(f"Произошла ошибка, сохранил без имени 🙄") 
    await state.clear()
    