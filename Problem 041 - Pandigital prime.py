from time import perf_counter
perf_counter()

def is_prime(n):
    n = int(n)
    if n == 2:
        return True
    if n < 2:
         return False
    if n % 2 == 0:
         return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def nr_list(n):
    result = []
    while n > 0:
        result.append(str(n))
        n -= 1
    return sorted(result)


def is_pandigital(number):
    number = str(number)
    if len(set(number)) == len(number):
        if sorted(number) == nr_list(len(number)):
            return True
        else:
            return False
    else:
        return False




for i in range(7654321, 1, -2): #7654321 is de grootst mogelijke pandigital prime want acht cijfers is altijd deelbaar door 3 en negen ook
    if is_pandigital(i):
        if is_prime(i):
            print(i)
            break

print("%0.4f" % perf_counter(), 'sec')