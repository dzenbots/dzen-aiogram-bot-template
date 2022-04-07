from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandHelp

from keyboards.default import get_user_reply_markup
from loader import dp
from utils.db_api.sqlite_api import User
from utils.set_bot_commands import set_commands_for_unauth_users


@dp.message_handler(CommandHelp(), in_group='Unauthorized', state='*', chat_type='private')
async def bot_help(message: types.Message, state: FSMContext):
    await state.finish()
    text = (
        "Дождитесь предоставления доступа к функциям бота администратором системы.",
        "Напоминаю - чтобы узнать ваш ID в системе, воспользуйтесь командой <b>Узнать свой ID</b> в меню данного бота"
    )
    await message.answer("\n".join(text))
    await set_commands_for_unauth_users(dp=dp, chat_id=message.from_user.id)


@dp.message_handler(CommandHelp(), state='*', chat_type='private')
async def bot_help(message: types.Message, state: FSMContext):
    await state.finish()
    user = User.get(telegram_id=message.from_user.id)
    text = (
        "Доступ к функциям бота предоставлен.",
        "Чтобы узнать, какие функции вам доступны, нажмите на кнопку <b>На главную</b> ниже."
    )
    await message.answer("\n".join(text), reply_markup=get_user_reply_markup(user))