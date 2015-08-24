answer = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        answer += i
print(answer)

#Or the alternative one liner:
print(sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]))