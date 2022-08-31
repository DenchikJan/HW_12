class Player:
    """
    Класс игрок
    """
    def __init__(self, user_name, user_words=[]):
        self.user_name = user_name
        self.user_words = user_words

    def cnt_user_words(self):
        return len(self.user_words)

    def app_user_words(self, user_word):
        self.user_words.append(user_word)

    def user_word_in_user_words(self, user_word):
        if user_word in self.user_words:
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.user_name}, {self.user_words}"
