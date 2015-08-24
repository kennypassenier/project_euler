def test(n):
    answers = []
    for a in range(1, int(n/3)+1 , 1):
        for b in range(1, int(n/3*2)+1, 1):
            for c in range(1, n, 1):
                if a < b:
                    if b < c:
                        if a + b + c == n:
                            answers.append(str(a) + ':' + str(b) + ':' + str(c))
    return answers


def is_pythagorean_triplet(a, b, c):
    if a >= b:
        if b >= c:
            return False
    return a ** 2 + b ** 2 == c ** 2


for i in test(1000):
    a, b, c = i.split(':')
    a, b, c = int(a), int(b), int(c)
    if is_pythagorean_triplet(a, b, c):
        print(a, b, c, 'are the members of the pythagorean triplet equalling 1k')
        print(a * b * c)
