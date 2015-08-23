
def digits_are_sum_of_nth_power(number, nthpower):
    number = str(number)
    answer = 0
    for i in number:
        answer += int(i) ** nthpower
    if int(number) == answer:
        return True
    else:
        return False
results = []
for i in range(2, 1000000):
    print(i)
    if digits_are_sum_of_nth_power(i, 5):
        results.append(i)
print(sum(results))