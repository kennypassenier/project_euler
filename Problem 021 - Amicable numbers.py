from math import sqrt


def get_proper_divisors(n):
    #returns a list with all the factors of n without n itself.
    factor_list = []
    result = list(set(factor_list))
    counter = 1
    while counter <= sqrt(n):
        result = sorted(list(set(factor_list)))
        if n % counter == 0:
            if counter in result:
                return result[:-1]
            else:
                factor_list.append(counter)
                factor_list.append(int(n / counter))
                counter += 1
        else:
            counter += 1
    else:
        return result[:-1]


def factor_sum(value):
    #returns the sum of the factors of value
    result = 0
    for i in get_proper_divisors(value):
        result += i
    return result


def is_amicable(value):
    #True if amicable, false if not
    test = sum(get_proper_divisors(value))
    return sum(get_proper_divisors(test)) == value and test != value


print(sum([x for x in range(1, 10000) if is_amicable(x)]))