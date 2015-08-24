from itertools import permutations

print(sorted([''.join(x) for x in permutations('0123456789')])[999999])
