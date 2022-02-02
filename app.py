from aiogram import executor
from peewee import SqliteDatabase

from loader import dp
# import middlewares, filters, handlers
from utils.db_api.sqlite_models import initialize_sqlite_db
from utils.notify_admins import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    if dispatcher.bot['database'] is not None:
        if isinstance(dispatcher.bot['database'], SqliteDatabase):
            initialize_sqlite_db()
    import middlewares
    import filters
    import handlers
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def on_shutdown(dispatcher):
    await on_shutdown_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown,
                           skip_updates=True)
