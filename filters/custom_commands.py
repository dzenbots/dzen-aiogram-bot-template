from aiogram.dispatcher.filters import Command


class GetMyID(Command):

    def __init__(self):
        super().__init__(['get_my_id'])


class FindUserCommand(Command):

    def __init__(self):
        super().__init__(['find_user'])
