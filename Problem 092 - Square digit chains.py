from time import perf_counter
perf_counter()

def square_digit_chain(n):
    new_n = 0
    str_n = str(n)
    while str_n != "1" and str_n != "89":
        for digit in str_n:
            new_n += int(digit) ** 2
        str_n = str(new_n)
        new_n = 0
    if str_n == "1":
        return 1
    elif str_n == '89':
        return 89
    else:
        return False
print(square_digit_chain(44))
print(square_digit_chain(85))

eighty_nines = []

for i in range(1, 10000000):
    print(i)
    if square_digit_chain(i) == 89:
        eighty_nines.append(i)
print(len(eighty_nines))

print("%0.4f" % perf_counter(), 'sec')