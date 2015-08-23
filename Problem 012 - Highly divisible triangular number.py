from math import sqrt
def tri_number(n):
    Tn = (n*(n+1))/2
    return int(Tn)
#A triangular number is calculated as: T(n) = n(n+1)/2

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


iterator = 1
factorlist = []
while len(factorlist) < 500:
    factorlist = getFactors(tri_number(iterator))
    print(str(iterator))
    print('The amount of factors for this number and its triangular number are are: ' + str(len(factorlist)) + ' ' + str(tri_number(iterator)))
    iterator += 1

#answer = 12375 iterations