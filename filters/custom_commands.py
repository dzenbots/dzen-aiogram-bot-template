from aiogram.dispatcher.filters import Command


class GetMyID(Command):

    def __init__(self):
        super().__init__(['get_my_id'])


class UsersCommand(Command):

    def __init__(self):
        super().__init__(['users'])


class GroupsCommand(Command):

    def __init__(self):
        super().__init__(['groups'])
