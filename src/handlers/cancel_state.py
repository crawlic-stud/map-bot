from aiogram import types, F
from aiogram.fsm.context import FSMContext

from config import dp


CANCEL = "cancel"

cancel_button = types.InlineKeyboardButton(text="Пропустить ➡️", callback_data=CANCEL)


@dp.callback_query(F.data == CANCEL)
async def cancel_any_state(_: types.CallbackQuery, state: FSMContext):
    await state.clear()
