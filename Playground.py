
from euler import is_possible_prime
for i in range(2, 1000):
    if is_possible_prime(i):
        print('{} is a possible prime number.'.format(i))

from euler import is_prime
for i in range(1, 1000):
    if is_prime(i):
        print('{} is a prime number'.format(i))

