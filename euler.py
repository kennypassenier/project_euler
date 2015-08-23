import random
from math import sqrt

_mrpt_num_trials = 5 # number of bases to test

def is_possible_prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """

    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True # no base tested showed n as composite

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


def get_factors(n): #Returns a list of factors in integer form
    factor_list = [n]
    result = list(set(factor_list))
    counter = 1
    while counter <= sqrt(n):
        result = list(set(factor_list))
        if n % counter == 0:
            if counter in result:
                return result
            else:
                factor_list.append(counter)
                factor_list.append(int(n / counter))
                counter += 1
        else:
            counter += 1
    else:
        return result

def main():
    pass

if __name__ == '__main__':
    main()