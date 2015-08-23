
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

condition = False
counter = 0
bouncy_numbers = []
while condition == False:
    counter += 1
    print(counter)
    if is_bouncy(counter):
        bouncy_numbers.append(counter)
    print(len(bouncy_numbers) / counter * 100)
    percentage = len(bouncy_numbers) / counter * 100
    if percentage == 99:
        condition = True
        print('The number is', counter)
