from euler import is_prime

answer = 0
counter = 0
prime_counter = 0
while prime_counter != 10001:
    counter += 1
    if is_prime(counter):
        prime_counter += 1
        answer = counter
print(answer)