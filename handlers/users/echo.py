from aiogram import types

from loader import dp


@dp.message_handler(state=None, chat_type='private')
async def bot_echo(message: types.Message):
    await message.answer(f"Я Вас не понимаю. Воспользуйтесь доступными Вам функциями.")
