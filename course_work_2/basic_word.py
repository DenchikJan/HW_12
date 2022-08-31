class BasicWord:
    """
    Класс слова.
    Состоит из полей word "исходное слово" и sub_words "набор доступных подслов"
    И методов in_word_sub_words(user_word) "проверка вхождения введеного слова в список подслов"
    и cnt_sub_words "подсчета колличества подслов"
    """
    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def in_word_sub_words(self, user_word):
        if user_word in self.sub_words:
            return True
        else:
            return False

    def cnt_sub_words(self):
        return len(self.sub_words)

    def __repr__(self):
        return f"{self.word}, {self.sub_words}"
