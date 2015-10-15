from euler import is_possible_prime as is_prime
import random
from time import perf_counter

perf_counter()


def test_for_prime_pattern(n):
    square = n ** 2
    return [square + 1, square + 3, square + 7, square + 9, square + 13, square + 27]


def primes_in_range(mini, maxi):
    results = []
    for i in range(mini, maxi + 1, 2):
        if is_prime(i):
            results.append(i)
    return len(results)


answers = []
for i in range(150000000, 0, -1):
    print(i)
    temp = test_for_prime_pattern(i)
    if all(map(is_prime, temp)):
        if len(temp) == primes_in_range(temp[0], temp[-1]):
            answers.append(i)

print('The solution is {}'.format(sum(answers)))
print('The script took {:.2f} seconds to run'.format(perf_counter()))