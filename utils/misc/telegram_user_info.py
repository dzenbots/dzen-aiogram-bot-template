from utils.db_api.sqlite_api import User, Group, GroupsOfUsers


def get_telegram_user_info(user: User):
    text = ('Информация о пользователе:',
            '',
            f'<b>ID</b>: {user.telegram_id}',
            '',
            f'<b>Фамилия</b>: {user.first_name}',
            f'<b>Имя</b>: {user.second_name}',
            f'<b>Отчество</b>: {user.third_name}',
            # f'Должность: {user.position}',
            # f'Номер телефона: {user.phone_number}',
            # f'Email: {user.email}',
            f''
            '',
            '<b>Член следующих групп:</b>',
            )
    for group in Group.select(Group).join(GroupsOfUsers).join(User).where(
            User.id == user.id):
        if group.group_name == 'Unauthorized':
            continue
        text = text + (f'{group.group_name}',)
    return '\n'.join(text)
