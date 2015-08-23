
def roman_to_int(n):
    n = str(n)
    result = 0
    while len(n) > 1:
        if n[0] == 'I':
            if n[1] == 'V':
                result += 4
                n = n[2:]
            elif n[1] == 'X':
                result += 9
                n = n[2:]
            else:
                result += 1
                n = n[1:]
        elif n[0] == 'V':
            result += 5
            n = n[1:]
        elif n[0] == 'X':
            if n[1] == 'L':
                result += 40
                n = n[2:]
            elif n[1] == 'C':
                result += 90
                n = n[2:]
            else:
                result += 10
                n = n[1:]
        elif n[0] == 'L':
            result += 50
            n = n[1:]
        elif n[0] == 'C':
            if n[1] == 'D':
                result += 400
                n = n[2:]
            elif n[1] == 'M':
                result += 900
                n = n[2:]
            else:
                result += 100
                n = n[1:]
        elif n[0] == 'D':
            result += 500
            n = n[1:]
        elif n[0] == 'M':
            result += 1000
            n = n[1:]
        else:
            return 'Something has gone horribly wrong'
    if len(n) == 1:
        if n == 'I':
            result += 1
        elif n == 'V':
            result += 5
        elif n == 'X':
            result += 10
        elif n == 'L':
            result += 50
        elif n == 'C':
            result += 100
        elif n == 'D':
            result += 500
        elif n == 'M':
            result += 1000
        else:
            return 'Something else has gone horribly wrong'
    return result


def highest_decimal_value(n):
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    result = []
    for i in values:
        if i <= n:
            result.append(i)
    return max(result)

def int_to_roman(n):
    numerals = {1:'I',
                4:'IV',
                5:'V',
                9:'IX',
                10:'X',
                40:'XL',
                50:'L',
                90:'XC',
                100:'C',
                400:'CD',
                500:'D',
                900:'CM',
                1000:'M'}
    result = ""
    while n > 0:
        m = highest_decimal_value(n)
        n -= m
        result += numerals[m]
    return result


f = open("roman.txt", 'r')
data = []
answer = 0
for line in f:
    data.append(line.strip())
f.close()
for i in data:
    temp = roman_to_int(i)
    temp_two = int_to_roman(temp)
    answer += len(i) - len(temp_two)
print(answer)