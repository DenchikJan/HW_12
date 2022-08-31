from random import choice

def get_word():

    """Вадает случайное слово из встроенного документа"""

    with open('words.txt') as file:
        words = file.read().split("\n")

    return choice(words)
