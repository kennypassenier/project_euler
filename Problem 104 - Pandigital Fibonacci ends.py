from time import perf_counter
from tqdm import *

perf_counter()

# (Public) Returns F(n).
def fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

def is_pandigital(number):
    number = str(number)
    if "0" in number:
        return False
    if len(set(number)) == len(number):
        return True
    else:
        return False

def has_pandigital_ends(number):
    number = str(number)
    if is_pandigital(number[0:9]):
        if is_pandigital(number[-9:]):
            return True
        else:
            return False
    else:
        return False
"""
counter = 329000
while has_pandigital_ends(fibonacci(counter)) == False:
    print(counter)
    counter += 1
else:
    print('The answer is', counter)
    print(len(fib(counter)))

#extremely slow :(
"""
for i in tqdm(range(1, 330000)):
    fibonacci(i)
print('0.4f' % perf_counter(), 'sec')