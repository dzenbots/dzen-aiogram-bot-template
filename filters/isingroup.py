from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery

from utils.db_api.sqlite_api import User, Group, GroupsOfUsers


class IsInGroupFilter(BoundFilter):
    key = 'in_group'

    def __init__(self, in_group):
        self.in_group = in_group

    async def check(self, call: CallbackQuery):
        try:
            user = User.get(telegram_id=call.from_user.id)
        except Exception:
            return False
        if user in User.select(User).join(GroupsOfUsers).join(Group). \
                where(Group.group_name == self.in_group):
            return True
        return False
