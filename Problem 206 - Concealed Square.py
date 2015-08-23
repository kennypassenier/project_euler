
def is_concealed_square(n):
    sq = str(n ** 2)
    if len(sq) == 19:
        if sq[0] == "1":
            if sq[2] == "2":
                if sq[4] == "3":
                    if sq[6] == "4":
                        if sq[8] == "5":
                            if sq[10] == "6":
                                if sq[12] == "7":
                                    if sq[14] == "8":
                                        if sq[16] == "9":
                                            if sq[18] == "0":
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
