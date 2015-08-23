from itertools import permutations

def is_in_lexicographic_order(number):
    temp = str(number)[0]
    for i in str(number)[1:-1]:
        if int(i) > int(temp):
            temp = int(i)
        else:
            return False
    return True

answer_list = []
list = ["0", "1", "2", "3", "4", '5', '6', '7', '8', '9']
for i in permutations(list):
    temp = ''.join(i)
    answer_list.append(temp)

print(sorted(answer_list)[999999])