from itertools import permutations

def permu(n):
    n = str(n)
    answer = []
    for i in  permutations(n):
        answer.append(''.join(i))
    return answer

def pandigital_products(n):
    n = str(n)
    count = 1
    counter = count + 1
    a = int(n[0:count])
    b = int(n[count:counter])
    c = int(n[counter:])
    while count <= len(n) - 2:
        counter = count + 1
        a = int(n[0:count])
        b = int(n[count:counter])
        c = int(n[counter:])
        while counter <= len(n) - 1:
            a = int(n[0:count])
            b = int(n[count:counter])
            c = int(n[counter:])
            if a * b == c:
                return str(c)
            counter += 1
        count += 1
    return False

results = []
lijst = permu(123456789)
counter = 1
for i in lijst:
    print(len(lijst) - counter)
    counter += 1
    if pandigital_products(i) != False:
        results.append(int(pandigital_products(i)))
print(results)
print(sum(set(results)))