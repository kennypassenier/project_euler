def is_palindrome(a):
    a = str(a)
    b = a[::-1]
    if a == b:
        return True
    else:
        return False

def add_reverse(a):
    a = str(a)
    b = a[::-1]
    return int(a) + int(b)

def is_lychrel_number(n):
    counter = 0
    lychrel_test = n
    while counter <= 50:
        lychrel_test = add_reverse(lychrel_test)
        if is_palindrome(lychrel_test):
            return False
        counter += 1
    return True

result = 0
for i in range(10000):
    if is_lychrel_number(i):
        result += 1
print(result)