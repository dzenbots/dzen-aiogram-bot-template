import logging

from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(dp.bot.get('config').tg_bot.admin_id, "Бот Запущен")

    except Exception as err:
        logging.exception(err)


async def on_shutdown_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(dp.bot.get('config').tg_bot.admin_id, "Бот остановлен")

    except Exception as err:
        logging.exception(err)
