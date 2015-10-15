from time import perf_counter
perf_counter()

def are_all_odd_integers(n):
    m = str(n)
    odd = ["1", "3", "5", "7", "9"]
    if len(m) == 1:
        return False
    for i in m:
        if not i in odd:
            return False
    return True


def are_same_number(n):
    n = str(n)
    for i in range(0, len(n)):
        if not n[0] == n[i]:
            return False
    return True

def mirror_number(n):
    n = str(n)
    result = n[::-1]
    result = int(result)
    return result

def is_reversible(n):
    str_number = str(n)
    if str_number[0] == "0":
        return False
    if str_number[-1] == "0":
        return False
    else:
        if are_all_odd_integers(n + mirror_number(n)):
            return True
        else:
            return False


answer = 0
for i in range(1, 100000000):
    if is_reversible(i):
        print(i)
        answer += 1
print(answer)


print("%0.4f" % perf_counter(), 'sec')