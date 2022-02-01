import logging

import gspread_asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from data.config import load_config

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)
logger.info("Starting bot")
config = load_config(".env")

storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

google_client_manager = gspread_asyncio.AsyncioGspreadClientManager(
    config.misc.scoped_credentials
)

bot['config'] = config
bot['google_client_manager'] = google_client_manager

dp = Dispatcher(bot, storage=storage)
