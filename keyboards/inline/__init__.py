from aiogram.utils.callback_data import CallbackData
from . import active_directory

telegram_user_cb_data = CallbackData('Tuser', 'func', 'user_id')

telegram_user_editing_data = CallbackData('TEdit', 'user_id', 'param')
