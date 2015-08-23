from itertools import permutations, combinations

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

def permu(data): #alleen voor primes
    temp = []
    answer = []
    data = str(data)
    result = permutations(data)
    for i in result:
            temp.append("".join(i))
    for i in temp:
        if is_prime(int(i)):
            answer.append(int(i))
    return answer

results = []
primes = []
for i in range(1000, 10000):
    if is_prime(i):
        primes.append(i)

for prime in primes:
    temp = []
    for permutation in permu(prime):
        if len(str(permutation)) == 4:
            if is_prime(permutation):
                temp.append(permutation)
    temp = set(temp)
    if len(temp) >= 3:
        results.append(sorted(list(temp)))

final_results = []
for listi in results:
    print('Printing the list with candidates for the mathematical sequence')
    print(listi)
    for i in combinations(listi, 2):
        print('Printing all possible combinations of two numbers withing the list of candidates')
        print(i)
        print('Printing i[0] and i[1]', i[0], i[1])
        very_temp = max(i[0], i[1]) - min(i[0], i[1])

        print('Printing very_temp', very_temp)
        number_to_check = very_temp + max(i[0], i[1])
        if number_to_check in listi:
            print('We have a match!')
            final_results.append([i[0], i[1], number_to_check])

print(final_results)