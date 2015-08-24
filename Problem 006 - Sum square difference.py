sum_square = 0
square_sum = 0

for i in range(1, 101):
    print(i)
    sum_square += i**2
    square_sum += i
square_sum = square_sum ** 2
list = [sum_square, square_sum]
result = max(list)-min(list)
print(sum_square, square_sum, result)