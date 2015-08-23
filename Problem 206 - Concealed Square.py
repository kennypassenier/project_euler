
def is_concealed_square(n):
    sq = str(n ** 2)
    if len(sq) == 19 and sq[::2]==list('1234567890'):
        return True
    return False

condition = True
counter = 0
while condition:
    counter += 1
    print(counter)
    if is_concealed_square(counter):
        answer = counter
        condition = False
print(answer)
