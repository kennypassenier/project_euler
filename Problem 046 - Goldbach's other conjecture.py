from euler import is_prime
def primes_below_this_number(n):
    return [x for x in range(1, n) if is_prime(x)]

def can_be_written_as_sum_of_prime_and_twice_a_square(n):
    counter = 1
    for prime in primes_below_this_number(n):
        condition = False
        while condition == False:
            temp_number = prime + 2 * counter ** 2
            if n == temp_number:
                return True
            elif n > temp_number:
                counter += 1
            else:
                counter = 1
                condition = True
    return False

win = False
counter = 3
while win == False:
    print(counter)
    if is_prime(counter) == False:
        if can_be_written_as_sum_of_prime_and_twice_a_square(counter) == False:
            print('The answer is {}'.format(counter))
            win = True
        else:
            counter += 2

    else:
        counter += 2


print(can_be_written_as_sum_of_prime_and_twice_a_square(840))