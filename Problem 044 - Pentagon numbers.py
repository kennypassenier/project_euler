from math import sqrt

def is_natural(n):
    if n % 1 == 0:
        return True
    else:
        return False

def is_pentagonal_number(n):
    n = int(n)
    answer = (1 + sqrt((24 * n + 1))) / 6
    if is_natural(answer):
        return True
    else:
        return False

def pentagon_number(n):
    return n * (3 * n - 1) / 2
condition = False
counter = 1
while condition == False:
    for k in range(1, 10000):
        pentj = pentagon_number(counter)
        pentk = pentagon_number(k)
        pentjk = pentj + pentk
        pentkj = max(pentj, pentk) - min(pentj, pentk)
        if is_pentagonal_number(pentjk):
            print(counter, k)
            if is_pentagonal_number(pentkj):
                print('Found it!')
                print(pentkj)
                condition = True
    counter += 1
