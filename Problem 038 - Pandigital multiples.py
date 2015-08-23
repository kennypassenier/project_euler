
def is_pandigital(number):
    number = str(number)
    if "0" in number:
        return False
    if len(set(number)) == len(number):
        return True
    else:
        return False


def my_function(n):
    counter = 1
    string_number = str(n)
    while len(string_number) < 9:
        counter += 1
        string_number = string_number + str(n * counter)
    return int(string_number)


results = []
for i in range(1, 1000000):
    print(i)
    if is_pandigital(my_function(i)):
        results.append(my_function(i))

print(results)
answer = []
for i in results:
    if len(str(i)) == 9:
        answer.append(i)
print(answer)
print(max(answer))