def write_users_name(user_name, earned_points):

    """ Записывает в файл имя игрока и его результат """

    with open('users.txt', 'a', encoding="utf-8") as file:
        content = file.write(f"{user_name} {earned_points}\n")
