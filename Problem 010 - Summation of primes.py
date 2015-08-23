from euler import is_prime
from tqdm import *

answer = 0
for i in tqdm(range(2000000, 1, -1)):
    if is_prime(i):
        answer += i
print(answer)