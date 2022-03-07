from aiogram.dispatcher.filters.state import StatesGroup, State


class FindUserState(StatesGroup):
    wait_for_id = State()


class GroupsEditState(StatesGroup):
    wait_for_name = State()
