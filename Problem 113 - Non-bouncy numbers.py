

def is_increasing_number(n):
    n = str(n)
    m = n[0]
    n = n[1:]
    while len(n) > 0:
        if int(n[0]) >= int(m):
            m = n[0]
            n = n[1:]
        else:
            return False
    return True


def is_decreasing_number(n):
    n = str(n)
    m = n[0]
    n = n[1:]
    while len(n) > 0:
        if int(n[0]) <= int(m):
            m = n[0]
            n = n[1:]
        else:
            return False
    return True

def is_bouncy(n):
    if is_increasing_number(n):
        return False
    elif is_decreasing_number(n):
        return False
    else:
        return True

answer = []
for i in range(10**100, 1, -1):
    print(i)
    if is_bouncy(i) == False:
        answer.append(i)
print(len(answer))