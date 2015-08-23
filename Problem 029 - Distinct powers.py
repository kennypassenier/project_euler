answer = []
for a in range(2, 101):
    for b in range(2, 101):
        answer.append(a ** b)
print(answer)
print(set(answer))
print(len(answer))
print(len(set(answer)))
