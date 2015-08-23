from time import perf_counter
perf_counter()

result_list = [2, 5]
def is_prime(n):
    n = int(n)
    if n == 2:
        return True
    if n < 2:
         return False
    if n % 2 == 0:
         return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def rotate(n):
    #rotate all numbers and return a list
    rotations = []
    m = str(n)
    m_list = list(m)
    for i in range(0, len(m)):
        m_list.append(m_list[0])
        m_list.pop(0)
        list_to_int = "".join(m_list)
        rotations.append(list_to_int)
    return rotations

def is_circular_prime(n):
    np = [0, 2, 4, 5, 6, 8]
    y = str(n)
    for j in y:
        if int(j) in np:
            return False
    if is_prime(n) == False:
        return False
    m = rotate(n)
    is_circ_prime = True
    for i in m:
        if not is_prime(i):
            is_circ_prime = False
    return is_circ_prime


for i in range(1, 1000000, 2):
    print(i)
    if is_circular_prime(i):
        result_list.append(i)
result_list.sort()
print(result_list)
print(len(result_list))

print("%0.4f" % perf_counter(), 'sec')
