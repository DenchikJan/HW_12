from random_word import get_word
#from shuffle_word import sh_word
from count_words import cnt_words
from users import write_users_name
from history import histiry

words = []
earned_points = 0

user_name = input("Введите ваше имя: ")

input("Нажмите Enter для начала игры. Если устнете играть, введите слово 'стоп'")

# Проверка на конец файла (все ли слова уже разгаданы)
while len(words) < cnt_words():
    word = get_word()
    word_2 = sh_word(word)
    if word not in words:
        print(f"Угадайте слово: {word_2}")
        user_response = input()
        words.append(word)
        # Проверка на выход из игры или продолжение
        if user_response == "стоп":
            print(f"Игра завершина.\n")
            break
        else:
            if word == user_response:
                print(f"Верно! Вы получаете 10 очков.\n")
                earned_points += 10
            else:
                print(f"Неверно! Верный ответ – {word}.\n")
    else:
        continue

write_users_name(user_name, earned_points)

histiry()
