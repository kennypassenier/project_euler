from itertools import permutations

def permu(data):
    temp = []
    answer = []
    data = str(data)
    result = permutations(data)
    for i in result:
            temp.append("".join(i))
    for i in temp:
        answer.append(int(i))
    return answer

def permuted_multiple(n):
    temp = permu(n)
    if 2 * n in temp:
        if 3 * n in temp:
            if 4 * n in temp:
                if 5 * n in temp:
                    if 6 * n in temp:
                        return True


condition = False
counter = 9
while condition == False:
    counter += 1
    if permuted_multiple(counter):
        print(counter)
        condition = True
    else:
        print(counter)