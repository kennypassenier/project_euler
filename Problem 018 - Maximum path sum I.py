
def read_file(a):
    #Reads the whole file, returns lists in a list
    with open(a, 'r') as file:
        result = []
        for line in file:
            result.append(line.rstrip().split())
        return result

data = read_file("data.txt")
for i in range(1, len(data))[::-1]:
    for j in range(0, len(data[i-1])):
        data[i - 1][j] = str(int(data[i - 1][j]) + max(int(data[i][j]), int(data[i][j + 1])))

print(data[0])