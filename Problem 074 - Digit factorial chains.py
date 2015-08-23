from math import factorial

def factorial_sum(number):
    answer = 0
    for digit in str(number):
        answer += factorial(int(digit))
    return answer

def factorial_chain(number):
    result = [number]
    identical = False
    while identical == False:
        temp = factorial_sum(number)
        if temp in result:
            identical = True
        else:
            result.append(temp)
            number = result[-1]
    return result




counter = 0
for i in range(1, 1000000):
    if len(factorial_chain(i)) == 60:
        counter += 1
print(counter)