from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from loguru import logger

from keyboards.inline.active_directory.user_info import edit_telegram_user_keyboard
from loader import dp
from utils.db_api.sqlite_api import User, GroupsOfUsers, Group
from utils.misc.telegram_user_info import get_telegram_user_info


class NewPersonFilter(BoundFilter):
    key = 'new_user'

    def __init__(self, new_user: bool):
        self.value = new_user

    async def check(self, message: Message):
        try:
            user = User.get(telegram_id=str(message.chat.id))
        except Exception:

            new_user, created = User.get_or_create(telegram_id=message.from_user.id,
                                                   defaults={
                                                       'first_name': ' ',
                                                       'second_name': ' ',
                                                       'third_name': ' '
                                                   })
            unauth_group = Group.get(group_name='Unauthorized')
            GroupsOfUsers.get_or_create(user=new_user, group=unauth_group)
            admins = User.select(User).join(GroupsOfUsers).join(Group).where(Group.group_name == 'BotAdmins')
            for admin in admins:
                await dp.bot.send_message(text='Новая попытка подключения!\n\n' + get_telegram_user_info(new_user),
                                          chat_id=admin.telegram_id,
                                          reply_markup=edit_telegram_user_keyboard(new_user))
            logger.info(
                f'New connection. Person with id {message.chat.id} is added to unauthorized persons group')
            return self.value
        if user in User.select(User).join(GroupsOfUsers).join(Group).where(Group.group_name == 'Unauthorized'):
            return self.value
        else:
            return not self.value
