from itertools import combinations
from tqdm import *

def one_p_nr(pound):
    temp = int(pound * 100) + 1
    answer = []
    for i in range(1, temp + 1):
        answer.append(1)
    return answer
def two_p_nr(pound):
    temp = int(pound * 50) + 1
    answer = []
    for i in range(1, temp + 1):
        answer.append(2)
    return answer
def five_p_nr(pound):
    temp = int(pound * 20) + 1
    answer = []
    for i in range(1, temp + 1):
        answer.append(5)
    return answer
def ten_p_nr(pound):
    temp = int(pound * 10) + 1
    answer = []
    for i in range(1, temp + 1):
        answer.append(10)
    return answer
def twenty_p_nr(pound):
    temp = int(pound * 5) + 1
    answer = []
    for i in range(1, temp + 1):
        answer.append(20)
    return answer
def fifty_p_nr(pound):
    temp = int(pound * 2) + 1
    answer = []
    for i in range(1, temp + 1):
        answer.append(50)
    return answer
def one_pound_nr(pound):
    temp = pound + 1
    answer = []
    for i in range(1, temp + 1):
        answer.append(100)
    return answer
def two_pound_nr(pound):
    temp = int(pound / 2) + 1
    answer = []
    for i in range(1, temp + 1):
        answer.append(200)
    return answer

inputnr = int(input('How many pounds do you want the answer for? '))
print('Starting 1p')
oneplist = [x for x in one_p_nr(inputnr)]
print('Starting 2p')
twoplist = [x for x in two_p_nr(inputnr)]
print('Starting 5p')
fiveplist = [x for x in five_p_nr(inputnr)]
print('Starting 10p')
tenplist = [x for x in ten_p_nr(inputnr)]
print('Starting 20p')
twentyplist = [x for x in twenty_p_nr(inputnr)]
print('Starting 50p')
fiftyplist = [x for x in fifty_p_nr(inputnr)]
print('Starting 1P')
onepoundlist = [x for x in one_pound_nr(inputnr)]
print('Starting 2P')
twopoundlist = [x for x in two_pound_nr(inputnr)]
print('Starting Combilist')
combilist = oneplist + twoplist + fiveplist + tenplist + twentyplist + fiftyplist + onepoundlist + twopoundlist
print(combilist)
print('{} is the length of the list'.format(len(combilist)))

final_result = []
for i in range(inputnr * 100, 0, -1):
    for j in combinations(combilist, i):
        if sum(j) == inputnr * 100:
            if j not in final_result:
                final_result.append(j)
                print('Found a match! {}'.format(j))
                print(len(j))

print(final_result)
print(len(final_result))