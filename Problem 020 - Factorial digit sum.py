from math import factorial
factorial_number = factorial(100)
result = 0
for i in str(factorial_number):
    result += int(i)
print(result)