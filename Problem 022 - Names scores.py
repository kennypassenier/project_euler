def letter_score(n):
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


temp = []
with open('names.txt', 'r') as f:
    text_data = f.read()
print(text_data)
temp = text_data.split(',')
temp = sorted(temp)
data = []
for i in temp:
    data.append(i[1 : -1])

final_answer = 0
counter = 0
for name in data:
    counter += 1
    final_answer += letter_score(name) * counter
print(final_answer)
