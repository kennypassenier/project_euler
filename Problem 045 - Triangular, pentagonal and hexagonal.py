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

def is_triangle_number(n):
    answer = 0.5 * sqrt(8 * n + 1) - 0.5
    if is_natural(answer):
        return True
    else:
        return False

def hex_number(n):
    return n * (2 * n - 1)

counter = 144
condition = False
while condition == False:
    print(counter)
    if is_pentagonal_number(hex_number(counter)):
        if is_triangle_number(hex_number(counter)):
            print(hex_number(counter))
            condition = True
    counter += 1