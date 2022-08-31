import Json

class Question:

    def __init__(self, text_question, complexity_question, correct_answer, question_asked=False, user_answer=None):
        self.text_question = text_question
        self.complexity_question = complexity_question
        self.correct_answer = correct_answer
        self.question_asked = question_asked
        self.user_answer = user_answer
        self.score = self.complexity_question * 10

    def get_points(self):

        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """

        return self.score

    def is_correct(self):

        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """

        if self.correct_answer == self.user_answer:
            return True
        else:
            return False

    def build_question(self):

        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """

        return f"Вопрос: {self.text_question}\nСложность: {self.complexity_question}/5"

    def build_positive_feedback(self):

        """Возвращает :
        Ответ верный, получено __ баллов
        """

        return f"Ответ верный, получено {self.score} баллов"

    def build_negative_feedback(self):

        """Возвращает :
        Ответ неверный, верный ответ __
        """

        return f"Ответ неверный, верный ответ {self.correct_answer}"


cnt_positive_answer = 0
all_score = 0

for question in Json.questions:
    question = Question(question['q'], int(question['d']), question['a'])
    print(question.build_question())
    question.user_answer = input()
    if question.is_correct():
        print(question.build_positive_feedback())
        cnt_positive_answer += 1
        all_score += question.get_points()
    else:
        print(question.build_negative_feedback())
    print('---')

print(f"Вот и всё!\nОтвечено {cnt_positive_answer} вопроса из {len(Json.questions)}\nНабрано баллов: {all_score}")
input()
