from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import get_user_reply_markup
from loader import dp
from utils.db_api.sqlite_api import User
from utils.set_bot_commands import set_user_commands


@dp.message_handler(CommandStart(), new_user=True, state='*', chat_type='private')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    user = User.get(telegram_id=message.from_user.id)
    await set_user_commands(dp=dp, chat_id=message.from_user.id)
    await message.answer(
        text="\n".join(
            (
                "Для доступа к функциям бота обратитесь к администратору.",
                "",
                "Вам необходимо будет сообщить ваш ID. Для этого воспользуйтесь командой <b>Узнать свой ID</b> в меню."
            )
        ),
        reply_markup=get_user_reply_markup(user)
    )


@dp.message_handler(CommandStart(), new_user=False, state='*', chat_type='private')
async def bot_start_further(message: types.Message, state: FSMContext):
    await state.finish()
    user = User.get(telegram_id=message.from_user.id)
    await set_user_commands(dp=dp, chat_id=message.from_user.id)
    await message.answer(text=f"С возвращением! Для просмотра доступных Вам функций нажмите на кнопку <b>На главную</b>",
                         reply_markup=get_user_reply_markup(user))
