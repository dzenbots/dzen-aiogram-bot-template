from aiogram.dispatcher.filters.state import StatesGroup, State


class FindUserState(StatesGroup):
    wait_for_id = State()


class GroupsEditState(StatesGroup):
    choose_action = State()
    wait_for_group_name = State()
    confirmation = State()
