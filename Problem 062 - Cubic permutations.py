from itertools import permutations

def permutate_nr(n):
    result = []
    n = str(n)
    l = len(n)
    for permu in permutations(n):
        permunr = ''
        for number in permu:
            if number in '0123456789':
                permunr += number
        if permunr[0] != '0':
            result.append(int(permunr))
    return list(set(result))


def is_cubic(x):
    y, y1 = None, 2
    while y!=y1:
        y = y1
        y3 = y**3
        d = (2*y3+x)
        y1 = (y*(y3+2*x)+d//2)//d
    if y * y * y != x:
        return False
    return True #return y yields the solution itself


i = 5000
condition = False
while condition == False:
    i += 1
    icube = i ** 3
    print(i, icube)
    counter = 0
    for permu in permutate_nr(icube):
        if is_cubic(permu):
            print('{} is a cubic permutation of {}'.format(permu, icube))
            counter += 1
    if counter == 5:
        print('The final answer is {}'.format(icube))
        condition = True

'''Takes only five years to run'''