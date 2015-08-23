from euler import is_possible_prime as is_prime
from math import sqrt
def is_hamming_number(n, x): #standard hamming numbers have x = 5
    if n < 0:
        return False
    factor_list = [n]
    result = factor_list
    for counter in range(1, int(sqrt(n)) + 1):
        result = list(set(factor_list))
        if n % counter == 0:
            if is_prime(counter):
                if counter > x:
                    return False
            if is_prime(int(n / counter)):
                if int(n / counter) > x:
                    return False
                else:
                    factor_list.append(counter)
                    factor_list.append(int(n / counter))
                counter += 1
        else:
            counter += 1
    else:
        return result

hamming_numbers = 0
for i in range(100000000):
    if is_hamming_number(i, 5):
        print(i)
        hamming_numbers += 1
print(hamming_numbers)