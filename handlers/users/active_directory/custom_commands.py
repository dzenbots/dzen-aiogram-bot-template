from aiogram import types

from filters.custom_commands import UsersCommand, GroupsCommand
from loader import dp
from states.admins_states import FindUserState, GroupsEditState


@dp.message_handler(UsersCommand(), state='*', chat_type='private', in_group='Admins')
async def bot_start(message: types.Message):
    await FindUserState.wait_for_id.set()
    await message.answer(text='Пришли ID искомого пользователя')


@dp.message_handler(GroupsCommand(), state='*', chat_type='private', in_group='Admins')
async def bot_start(message: types.Message):
    await GroupsEditState.choose_action.set()
    await message.answer(text='Выбери действие с группами')

