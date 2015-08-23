from math import factorial


def digits_are_sum_of_factorial(number):
    number = str(number)
    answer = 0
    for i in number:
        answer += factorial(int(i))
    if int(number) == answer:
        return True
    else:
        return False
results = []
for i in range(3, 1000000):
    print(i)
    if digits_are_sum_of_factorial(i):
        results.append(i)
print(sum(results))