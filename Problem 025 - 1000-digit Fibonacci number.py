from time import perf_counter
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

counter = 0
while True:
    counter += 1
    if len(str(fibonacci(counter))) == 1000:
        print(counter)
        break
print("%0.9f" % perf_counter(), 'sec')