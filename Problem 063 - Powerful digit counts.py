

def how_many_n_digit_numbers_are_also_nth_power(exponent):
    answer_count = 0
    count = 0
    condition = True
    while condition:
        count += 1
        pow_count = count ** exponent
        if len(str(pow_count)) == exponent:
            answer_count += 1
            print(pow_count, len(str(pow_count)))
        elif len(str(pow_count)) > exponent:
            condition = False
    return answer_count

result = 0
for i in range(1, 100):
    result += how_many_n_digit_numbers_are_also_nth_power(i)
print(result)