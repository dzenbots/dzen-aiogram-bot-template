from typing import Union

from aiogram import Dispatcher
from peewee import Model, SqliteDatabase, CharField, ForeignKeyField

from loader import dp

# db = SqliteDatabase(database=dp.bot['config'].db.filename, pragmas={'foreign_keys': 1})

db: Union[SqliteDatabase, None] = dp.bot.get('database')


class SqliteBaseModel(Model):
    class Meta:
        database = db


class Group(SqliteBaseModel):
    group_name = CharField()


class User(SqliteBaseModel):
    telegram_id = CharField()
    first_name = CharField()
    second_name = CharField()
    third_name = CharField()


class GroupsOfUsers(SqliteBaseModel):
    user_id = ForeignKeyField(User, backref='groups')
    group_id = ForeignKeyField(Group, backref='users')


def on_startup_sqlite(dp: Dispatcher):
    db = dp.bot.get('database')
    if db:
        db.connect()
        db.create_tables([
            User,
            Group,
            GroupsOfUsers
        ], safe=True)
        master_group, created = Group.get_or_create(group_name='MasterAdmin')
        Group.get_or_create(group_name='Unauthorized')
        master_admin, created = User.get_or_create(telegram_id=dp.bot.get('config').tg_bot.admin_id,
                                                   defaults={
                                                       'first_name': '',
                                                       'second_name': '',
                                                       'third_name': '',

                                                   })
        GroupsOfUsers.get_or_create(user_id=master_admin.id, group_id=master_group.id)


def on_shutdown_sqlite(dp: Dispatcher):
    db = dp.bot.get('database')
    db.close()
