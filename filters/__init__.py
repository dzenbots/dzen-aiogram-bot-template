from aiogram import Dispatcher

from filters.isingroup import IsInGroupFilter
from filters.new_person import NewPersonFilter
from loader import dp


if __name__ == "filters":
    dp.filters_factory.bind(IsInGroupFilter)
    dp.filters_factory.bind(NewPersonFilter)
    pass
