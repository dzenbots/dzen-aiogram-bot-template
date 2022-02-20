from peewee import Model, SqliteDatabase

from loader import dp

db = SqliteDatabase(database=dp.bot['config'].db.filename, pragmas={'foreign_keys': 1})


class SqliteBaseModel(Model):
    class Meta:
        database = db


def on_startup_sqlite():
    db.connect()
    db.create_tables([

    ], safe=True)


def on_shutdown_sqlite():
    db.close()
