
from itertools import permutations

def permu(data):
    temp = []
    answer = []
    data = str(data)
    result = permutations(data)
    for i in result:
            temp.append("".join(i))
    for i in temp:
        if i[0] != '0':
            answer.append(int(i))
    return answer


def has_interesting_sub_string_property(n):
    n = str(n)
    if int(n[1:4]) % 2 == 0:
        if int(n[2:5]) % 3 == 0:
            if int(n[3:6]) % 5 == 0:
                if int(n[4:7]) % 7 == 0:
                    if int(n[5:8]) % 11 == 0:
                        if int(n[6:9]) % 13 == 0:
                            if int(n[7:10]) % 17 == 0:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
results = []
for i in permu(1234567890):
    if has_interesting_sub_string_property(i):
        results.append(i)
print(results)
print(sum(results))