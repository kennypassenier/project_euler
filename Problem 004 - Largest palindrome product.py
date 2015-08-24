def is_palindrome(a):
    a = str(a)
    return a == a[::-1]

results = []
for first_product in range(1000):
    for second_product in range(1000):
        if is_palindrome(first_product * second_product):
            results.append(first_product * second_product)
print(max(results))