from math import sqrt


def tri_number(n):
    return int((n*(n+1))/2)


def get_factors(n):
    factor_l = [n]
    result = list(set(factor_list))
    counter = 1
    while counter <= sqrt(n):
        result = list(set(factor_l))
        if n % counter == 0:
            if counter in result:
                return result
            else:
                factor_l.append(counter)
                factor_l.append(int(n / counter))
                counter += 1
        else:
            counter += 1
    else:
        return result


iterator = 0
factor_list = []
while len(factor_list) < 500:
    iterator += 1
    factor_list = get_factors(tri_number(iterator))
    print("{} has {} factors and its triangular number is {}".format(iterator, len(factor_list), tri_number(iterator))) #This was just to check up on progress.

print(iterator - 1)

#answer = 12375 iterations