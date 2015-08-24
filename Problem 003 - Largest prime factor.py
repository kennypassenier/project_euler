from time import clock
from math import sqrt
start = clock()
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

def getFactors(n):
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


for i in getFactors(123456789123456):
    if is_prime(i):
        print(i)
end = clock()

print(end - start)

#Takes around 42 seconds to run on my pc.