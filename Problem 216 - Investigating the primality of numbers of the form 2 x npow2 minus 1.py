from euler import is_possible_prime

def t_number(n):
    if n <= 1:
        raise ValueError('This cannot be smaller than 1')
    return 2 * n ** 2 - 1

primes = 0

for i in range(2, 50000000):
    print(i)
    if is_possible_prime(t_number(i)):
        primes += 1
print(primes)