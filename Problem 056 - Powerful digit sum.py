from time import clock


start = clock()

temp = []
answer = []
for a in range(1, 100):
    for b in range(1, 100):
        print('A', a, 'B', b, '=', a ** b)
        temp.append(a ** b)
for value in temp:
    dig_sum = 0
    for number in str(value):
        dig_sum += int(number)
    answer.append(dig_sum)
print('result:')
print(set(answer))
print(max(answer))

end = clock()
print(end - start)