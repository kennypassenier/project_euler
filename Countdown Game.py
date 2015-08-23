from datetime import datetime, timedelta
from random import randint


def populate_word_list():

    f = open("words2.txt", 'r')
    data = []
    answer = 0
    for line in f:
        data.append(line.strip())
    f.close()
    words = []
    for word in data:
        if len(word) >= 3:
            if len(word) <=9:
                words.append(word.lower())
    words = set(words)
    return words


def is_word_made_of_letters(word, letters):
    counter = 0
    for letter in word:
        if letter in letters:
            counter += 1
            letters.remove(letter)
        else:
            return False
    if counter == len(word):
        return True
    else:
        return False


def solve_word_game(word_list):
    answer = []
    letters = input('Enter the letters: ')
    for word in word_list:
        if is_word_made_of_letters(word, [x for x in letters]):
            answer.append(word)
    return sorted(answer, key=len, reverse=True)


def main():
    word_list = populate_word_list()
    print(solve_word_game(word_list))

def random_numbers_attempt(list_, target):
    a = datetime.now()
    b = a + timedelta(seconds=25)
    while datetime.now() <= b:
        pass


#--------------------------
main()
