import utils
import player

user_name = input("Введите свое имя\n")

print(f"Привет, {user_name}!")
user = player.Player(user_name)
word = utils.load_random_word()
print(f"Составте {word.cnt_sub_words()} слов из слова {word.word}\nСлова должны быть не короче 3 букв")
print(f"Чтобы закончить игру, угадайте все слова или напишите слово 'stop'\nПоехали, ваше первое слово?")
while user.cnt_user_words() < word.cnt_sub_words():
    user_word = input()
    if len(user_word) < 3:
        print("Слишком короткое слово")
    elif not word.in_word_sub_words(user_word):
        if user_word in ("stop", "стоп"):
            break
        else:
            print("Неверно")
    elif user.user_word_in_user_words(user_word):
        print("Уже использовано")
    else:
        user.app_user_words(user_word)
        print("Верно")

print(f"Игра завершена, вы угадали {user.cnt_user_words()} слов!")
