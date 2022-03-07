from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.db_api.sqlite_api import User, GroupsOfUsers, Group


def main_inline_user_keyboard(user: User):
    inline_keyboard = []
    # if user in User.select(User).join(GroupsOfUsers).join(Group).where(Group.group_name == 'Users'):
    #     inline_keyboard.append([
    #         InlineKeyboardButton(
    #             text=' 🆘 IT помоги!',
    #             url=IT_SUPPORT_TABLE_URL
    #         )
    #     ])
    # if user in User.select(User).join(GroupsOfUsers).join(Group).where(Group.group_name == 'Zavhoz'):
    #     pass
    # if user in User.select(User).join(GroupsOfUsers).join(Group).where(Group.group_name == 'IT'):
    #     inline_keyboard.append([
    #         InlineKeyboardButton(
    #             text=' 📋 Таблица заявок',
    #             url=IT_SUPPORT_TABLE_URL
    #         )
    #     ])

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
