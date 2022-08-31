def cnt_words():

    """ Считает количество слов в файле """

    cnt_words = 0
    with open('words.txt') as file:
        for i in file:
            cnt_words += 1
    return cnt_words
