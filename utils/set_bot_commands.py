from aiogram import types, Dispatcher
from aiogram.types import BotCommandScopeChat


async def set_default_commands(dp, chat_id):
    await dp.bot.set_my_commands(
        commands=[
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Помощь"),

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
