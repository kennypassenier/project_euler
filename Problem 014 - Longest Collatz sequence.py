from time import clock
start = clock()


def collatz_sequence(number):
    sequence = [number]

    while sequence[-1] != 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] / 2)
        else:
            sequence.append(sequence[-1] * 3 + 1)
    return sequence


longest_chain = 0
starting_number = 0
for i in range(1, 1000000):
    if len(collatz_sequence(i)) > longest_chain:
        longest_chain = len(collatz_sequence(i))
        starting_number = i
print('The answer is:', starting_number, 'with a chain length of:', longest_chain)
end = clock()
print(end - start)