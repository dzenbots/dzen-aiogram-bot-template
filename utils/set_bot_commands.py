from aiogram import types, Dispatcher
from aiogram.types import BotCommandScopeChat

from utils.db_api.sqlite_api import User, Group, GroupsOfUsers


async def set_default_commands(dp, chat_id):
    await dp.bot.set_my_commands(
        commands=[
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("get_my_id", "Узнать свой ID"),
            types.BotCommand("help", "Помощь"),
        ],
        scope=BotCommandScopeChat(chat_id=chat_id)
    )


async def set_admin_commands(dp, chat_id):
    await dp.bot.set_my_commands(
        commands=[
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("users", "Пользователи"),
            types.BotCommand("groups", "Группы"),
            types.BotCommand("help", "Помощь"),
            types.BotCommand("get_my_id", "Узнать свой ID"),
        ],
        scope=BotCommandScopeChat(chat_id=chat_id)
    )


async def set_commands_for_unauth_users(dp: Dispatcher, chat_id):
    await dp.bot.set_my_commands(
        commands=[
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("get_my_id", "Узнать свой ID"),
            types.BotCommand("help", "Помощь"),
        ],
        scope=BotCommandScopeChat(chat_id=chat_id)
    )


async def set_user_commands(dp: Dispatcher, chat_id):
    if 'Unauthorized' in [group.group_name for group in
                          Group.select(Group).join(GroupsOfUsers).join(User).where(User.telegram_id == chat_id)]:
        await set_commands_for_unauth_users(dp, chat_id)
    elif 'Admins' in [group.group_name for group in
                      Group.select(Group).join(GroupsOfUsers).join(User).where(User.telegram_id == chat_id)]:
        await set_admin_commands(dp, chat_id)
    else:
        await set_default_commands(dp, chat_id)
