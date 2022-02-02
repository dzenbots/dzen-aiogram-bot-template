from peewee import Model

from loader import dp


class BaseModel(Model):
    class Meta:
        database = dp.bot['database']

