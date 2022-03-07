from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from utils.db_api.sqlite_api import User, GroupsOfUsers, Group


def get_user_reply_markup(user: User):
    if user in User.select(User).join(GroupsOfUsers).join(Group).where(Group.group_name == 'Unauthorized'):
        return ReplyKeyboardRemove()
    else:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='На главную')
                ]
            ],
            resize_keyboard=True
        )