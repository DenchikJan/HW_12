import random
import basic_word
import requests


def load_random_word():
    """
    Вывод случайного слова из предложеного списка
    в формате словаря word: заданое слово subwords: список входящих слов
    """
    response = requests.get("https://jsonkeeper.com/b/I4HO")
    content = response.json()
    word = random.choice(content)
    word = basic_word.BasicWord(word["word"], word["subwords"])
    return word
