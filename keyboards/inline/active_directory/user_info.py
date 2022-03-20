from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline import telegram_user_cb_data, telegram_user_editing_data
from utils.db_api.sqlite_api import User


def edit_telegram_user_keyboard(user: User):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Изменить инфо',
                    callback_data=telegram_user_cb_data.new(
                        func='edit_info',
                        user_id=user.telegram_id
                    )
                )
            ],
            [
                InlineKeyboardButton(
                    text='Изменить группы',
                    callback_data=telegram_user_cb_data.new(
                        func='edit_groups',
                        user_id=user.telegram_id
                    )
                )
            ],
            [
                InlineKeyboardButton(
                    text='Закончить редактирование',
                    callback_data=telegram_user_cb_data.new(
                        func='finish_edit',
                        user_id=user.telegram_id
                    )
                )
            ],
        ]
    )


def get_edit_user_info_keyboard(target_user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Фамилия',
                    callback_data=telegram_user_editing_data.new(
                        user_id=target_user_id,
                        param='surname'
                    )
                ),
            ],
            [
                InlineKeyboardButton(
                    text='Имя',
                    callback_data=telegram_user_editing_data.new(
                        user_id=target_user_id,
                        param='name'
                    )
                ),
            ],
            [
                InlineKeyboardButton(
                    text='Отчество',
                    callback_data=telegram_user_editing_data.new(
                        user_id=target_user_id,
                        param='patronymic'
                    )
                ),
            ],
            [
                InlineKeyboardButton(
                    text='◀️ Вернуться к информации о пользователе',
                    callback_data=telegram_user_cb_data.new(
                        func='go_back',
                        user_id=target_user_id
                    )
                ),
            ],
        ]
    )
