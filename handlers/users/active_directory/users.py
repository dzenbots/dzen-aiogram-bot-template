from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import dp
from utils.db_api.sqlite_api import User


@dp.message_handler(state='*', chat_type='private', in_group='Admins')
async def find_user_by_tgID(message: Message, state: FSMContext):
    target_user: User = None
    try:
        target_user = User.get(telegram_id=message.text)
    except:
        await message.answer(f"Пользователь с ID {message.text} не найден.")
    if target_user is not None:
        user_info = '\n'.join([
            f'ID: <b>{target_user.telegram_id}</b>',
            f'Фамилия: {target_user.first_name}',
            f'Имя: {target_user.second_name}',
            f'Отчество: {target_user.third_name}'
        ])
