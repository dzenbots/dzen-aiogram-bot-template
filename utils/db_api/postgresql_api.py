import datetime
from typing import List
import sqlalchemy as sa
from aiogram import Dispatcher

from loguru import logger

from loader import dp


class BaseModel(dp.bot['database'].Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True

    created_at = dp.bot['database'].Column(
        dp.bot['database'].DateTime(True),
        server_default=dp.bot['database'].func.now()
    )
    updated_at = dp.bot['database'].Column(
        dp.bot['database'].DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=dp.bot['database'].func.now(),
    )


async def on_startup_postresql(dispatcher: Dispatcher):
    logger.info("Setup PostgreSQL Connection")
    await dp.bot['database'].set_bind()


async def on_shutdown_postresql(dispatcher: Dispatcher):
    bind = dp.bot['database'].pop_bind()
    if bind:
        logger.info("Close PostgreSQL Connection")
        await bind.close()
