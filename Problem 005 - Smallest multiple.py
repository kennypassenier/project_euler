global iterator_a

def divisible(n):
    iterator = 1
    while iterator < 21:
        if n % iterator == 0:
            iterator += 1
        else:
            return False
    else:
        return True
iterator_a = 1
while divisible(iterator_a) == False:
    print(str(iterator_a) + ' is false')
    iterator_a += 1
else:
    print(int(iterator_a))


#Answer = 232792560