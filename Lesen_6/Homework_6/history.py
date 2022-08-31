def histiry():

    """ Выводит из файла историю игр, общее количество игр и максимальный результат"""

    cnt_words = 0
    max_result = 0

    with open('users.txt') as file:
        for i in file:
            cnt_words += 1
            s = int(i.split(" ")[1])
            if s > max_result:
                max_result = s

    print(f"Всего игр сыграно: {cnt_words}\nМаксимальный рекорд: {max_result}")


histiry()
