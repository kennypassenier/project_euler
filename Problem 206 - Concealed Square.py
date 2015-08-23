
def is_concealed_square(n):
    sq = str(n ** 2)
    if len(sq) == 19 and sq[0] == "1" and sq[2] == "2" and sq[4] == "3" and sq[6] == "4" and sq[8] == "5" and sq[10] == "6" and sq[12] == "7" and sq[14] == "8" and sq[16] == "9" and sq[18] == "0":
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
