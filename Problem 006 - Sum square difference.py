sumsquare = 0
squaresum = 0

for i in range(1, 101):
    print(i)
    sumsquare += i**2
    squaresum += i
squaresum = squaresum **2
list = [sumsquare, squaresum]
result = max(list)-min(list)
print(sumsquare, squaresum, result)