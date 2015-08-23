from math import sqrt

def letter_score(n):
    n = str(n).lower()
    answer = 0
    transfer_dict = {'a':1,
                     "b":2,
                     'c':3,
                     'd':4,
                     'e':5,
                     'f':6,
                     'g':7,
                     'h':8,
                     'i':9,
                     'j':10,
                     'k':11,
                     'l':12,
                     'm':13,
                     'n':14,
                     'o':15,
                     'p':16,
                     'q':17,
                     'r':18,
                     's':19,
                     't':20,
                     'u':21,
                     'v':22,
                     'w':23,
                     'x':24,
                     'y':25,
                     'z':26}
    n = str(n).lower()
    for letter in n:
        answer += transfer_dict[letter]
    return answer


def reverse_triangle_number(n):
    answer = 0.5 * sqrt(8 * n + 1) - 0.5
    if answer%1 == 0:
        return True
    else:
        return False

triangles = 0

with open('words.txt', 'r') as f:
    text_data = f.read()
temp = text_data.split(',')
data = []
for i in temp:
    data.append(i[1 : -1])
test = 0
for i in data:
    test += 1
    if reverse_triangle_number(letter_score(i)):
        triangles += 1
print(triangles)