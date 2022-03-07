from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from keyboards.inline.main_user_keyboard import main_inline_user_keyboard
from loader import dp
from utils.db_api.sqlite_api import User


@dp.message_handler(Text(equals='На главную'), state='*', chat_type='private')
async def go_on_main(message: Message, state: FSMContext):
    await state.finish()
    user = User.get(telegram_id=message.from_user.id)
    await message.answer(text="Список доступных Вам функций:",
                         reply_markup=main_inline_user_keyboard(user))
