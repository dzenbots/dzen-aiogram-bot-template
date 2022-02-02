from peewee import Model

from loader import dp


class SqliteBaseModel(Model):
    class Meta:
        database = dp.bot['database']


def initialize_sqlite_db():
    dp.bot['database'].connect()
    dp.bot['database'].create_tables([

    ], safe=True)

