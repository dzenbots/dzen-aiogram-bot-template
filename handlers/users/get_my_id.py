from aiogram import types
from aiogram.dispatcher import FSMContext

from filters.custom_commands import GetMyID
from loader import dp


@dp.message_handler(GetMyID(), state='*', chat_type='private')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f'Ваш ID: {message.from_user.id}')
