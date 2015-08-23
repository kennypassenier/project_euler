from tqdm import *

def is_palindrome(a):
    a = str(a)
    if a == a[::-1]:
        return True
    else:
        return False

answer = 0
for i in tqdm(range(1, 1000000)):
    if is_palindrome(i):
        if is_palindrome(bin(i)[2:]):
            answer += i
print(answer)

