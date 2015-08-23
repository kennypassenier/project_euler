

def getFactors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    factors.pop() #Don't want self as factor
    return factors

def isPrime(n):
    """"precondition n is a nonnegative integer
postcondition:  return True if n is prime and False otherwise."""
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

iterator = 1
win_condition = False
while win_condition == False:
    temp_res = getFactors(iterator)
    temp_res = sorted(temp_res)
    counter = 0
    for i in temp_res:
        if isPrime(i):
            counter += 1
    if counter == 4:
        temp_res = getFactors(iterator + 1)
        temp_res = sorted(temp_res)
        counter = 0
        for i in temp_res:
            if isPrime(i):
                counter += 1
        if counter == 4:
            temp_res = getFactors(iterator + 2)
            temp_res = sorted(temp_res)
            counter = 0
            for i in temp_res:
                if isPrime(i):
                    counter += 1
            if counter == 4:
                temp_res = getFactors(iterator + 3)
                temp_res = sorted(temp_res)
                counter = 0
                for i in temp_res:
                    if isPrime(i):
                        counter += 1
                if counter == 4:
                    print('We have a winner!')
                    print(iterator)
                    print(getFactors(iterator))
                    for i in getFactors(iterator):
                        if isPrime(i):
                            print(i)
                    win_condition = True
                else:
                    print('Fail', getFactors(iterator))
                    print(iterator)
                    iterator += 1
            else:
                print('Faal', getFactors(iterator))
                print(iterator)
                iterator += 1
        else:
            print('Faalbal', getFactors(iterator))
            print(iterator)
            iterator += 1
    else:
        print('Faler', getFactors(iterator))
        print(iterator)
        iterator += 1



