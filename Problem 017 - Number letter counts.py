
def write_out_number(n):
    one_to_nineteen = {"1":'one',
                     "2":"two",
                     "3":'three',
                     "4":'four',
                     "5":'five',
                     "6":'six',
                     "7":'seven',
                     "8":'eight',
                     "9":'nine',
                     "10":'ten',
                     "11":'eleven',
                     "12":'twelve',
                     "13":'thirteen',
                     "14":'fourteen',
                     "15":'fifteen',
                     "16":'sixteen',
                     "17":'seventeen',
                     "18":'eighteen',
                     "19":'nineteen'}
    tens = {"1":'ten',
            "2":'twenty',
            "3":'thirty',
            "4":'forty',
            "5":'fifty',
            "6":'sixty',
            "7":'seventy',
            "8":'eighty',
            "9":'ninety'}
    hundreds = {"1":'onehundred',
                "2":'twohundred',
                "3":'threehundred',
                "4":'fourhundred',
                "5":'fivehundred',
                "6":'sixhundred',
                "7":'sevenhundred',
                "8":'eighthundred',
                "9":'ninehundred'}
    n = str(n)
    if len(n) == 4:
        return 'onethousand'
    elif len(n) == 3:
        if n[1:] in one_to_nineteen:
            return hundreds[n[0]] + 'and' + one_to_nineteen[n[1:]]
        if '0' not in n:
            return hundreds[n[0]] + 'and' + tens[n[1]] + one_to_nineteen[n[2]]
        elif n[1] == "0" and n[2] == "0":
            return hundreds[n[0]]
        elif n[1] == '0':
            return hundreds[n[0]] + 'and' + one_to_nineteen[n[2]]
        elif n[2] == '0':
            return hundreds[n[0]] + 'and' + tens[n[1]]

    elif len(n) == 2:
        if n in one_to_nineteen:
            return one_to_nineteen[n]
        else:
            if n[-1] == '0':
                return tens[n[0]]
            else:
                return tens[n[0]] + one_to_nineteen[n[1]]
    elif len(n) == 1:
        return one_to_nineteen[n]
    else:
        return 'Something has gone horribly wrong.'

result = 0
for i in range(1,1001):
    result += len(write_out_number(i))
print(result)