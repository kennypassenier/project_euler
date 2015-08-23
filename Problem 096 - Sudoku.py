from numpy import array, in1d

"""...................................................................................."""


def soduku_is_ready(): #returns True or False
    if any(in1d(data_array, 0)):
        return False
    return True

    #Als er geen nullen/False statements meer zijn in data_array

def column(n, data): #returns a list
    n -= 1
    result = []
    for i in range(0, 9):
        result.append(data[i, n])
    return result

def row(n, data): #returns a list
    n -= 1
    result = []
    for i in data[n]:
        result.append(i)
    return result

def block(n): #From left to right, top to bottom, not like standard cartesian coordinates of a quadrant
    result = []
    if n in [1, 4, 7]:
        for i in range(0, 3):
            for j in row(n+i, data_array)[0:3]:
                result.append(j)
    elif n in [2, 5, 8]:
        for i in range(0, 3):
            for j in row(n + i - 1, data_array)[3:6]:
                result.append(j)
    else:
        for i in range(0, 3):
            for j in row(n + i - 2, data_array)[6:9]:
                result.append(j)
    return result

def get_block_number(row_number, column_number): #returns an integer from 1-9 out of coordinates
    if row_number in [1, 2, 3]:
        if column_number in [1, 2, 3]:
            return 1
        elif column_number in [4, 5, 6]:
            return 2
        else:
            return 3
    if row_number in [4, 5, 6]:
        if column_number in [1, 2, 3]:
            return 4
        elif column_number in [4, 5, 6]:
            return 5
        else:
            return 6
    if row_number in [7, 8, 9]:
        if column_number in [1, 2, 3]:
            return 7
        elif column_number in [4, 5, 6]:
            return 8
        else:
            return 9



def candidates(row_number, column_number): #returns a list with all possible candidates
    result = []
    block_number = get_block_number(row_number, column_number)

    if data_array[row_number - 1, column_number - 1] != 0:
        result.append(data_array[row_number - 1, column_number - 1])
        return result

    for i in range(1, 10):
        if i not in row(row_number, data_array):
            if i not in column(column_number, data_array):
                if i not in block(block_number):
                    result.append(i)
    return result

def solve_single_candidate_squares(data): #When a square has just 1 candidate, that number goes into the square
    for i in range(1, 10):
        for j in range(1, 10):
            if len(candidates(i, j)) == 1:
                data[i - 1, j - 1] = candidates(i, j)[0]

#def solve_single_square_candidates(data):
    """#When a candidate number appears once in an area(row, column or block), that number goes into the square."""







"""...................................................................................."""


sudokudata = [[4, 6, 0, 3, 0, 1, 0, 0, 8],
              [0, 9, 0, 0, 4, 0, 0, 6, 0],
              [0, 0, 1, 0, 0, 0, 2, 0, 0],
              [6, 0, 0, 9, 0, 4, 5, 0, 7],
              [0, 5, 0, 0, 3, 0, 0, 8, 0],
              [9, 0, 0, 5, 0, 8, 0, 0, 3],
              [0, 0, 6, 0, 0, 0, 8, 0, 0],
              [0, 2, 0, 0, 8, 0, 0, 5, 0],
              [8, 0, 0, 1, 0, 7, 0, 0, 2]]
data_array = array(sudokudata)


"""...................................................................................."""

