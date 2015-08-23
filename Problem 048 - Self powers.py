def self_power_sum(number):
    answer = 0
    while number >= 1:
        print(number)
        answer+= number ** number
        number -= 1
    return answer


result = str(self_power_sum(1000))
print(result)
print(result[-10::])