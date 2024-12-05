from pathlib import Path

FILE_PATH = Path(__file__).parent / './test_input.txt'

def parse_text_file():
    matrix = []
    with open(FILE_PATH) as f: 
        for row in f:
            matrix.append(list(row.strip()))
    return(matrix)

MATRIX = parse_text_file()
X_LIMIT = len(MATRIX[0])
Y_LIMIT = len(MATRIX)

SEARCH_MATRIX_1 = [['M', None ,'S'], [None, 'A', None], ['M', None, 'S']]
SEARCH_MATRIX_2 = [['S', None ,'S'], [None, 'A', None], ['M', None, 'M']]
SEARCH_MATRIX_3 = [['S', None ,'M'], [None, 'A', None], ['S', None, 'M']]
SEARCH_MATRIX_4 = [['M', None ,'M'], [None, 'A', None], ['S', None, 'S']]

def match(x, y):
    matched_one = False
    for target in [SEARCH_MATRIX_1, SEARCH_MATRIX_2, SEARCH_MATRIX_3, SEARCH_MATRIX_4]:
        center = MATRIX[x][y] == target[1][1]
        north_east = MATRIX[x+1][y-1] == target[2][0]
        south_east = MATRIX[x+1][y+1] == target[2][2]
        south_west = MATRIX[x-1][y+1] == target[0][2]
        north_west = MATRIX[x-1][y-1] == target[0][0]
        matched_one = matched_one or (center and north_east and south_east and south_west and north_west)
    return int(matched_one)

def search_submatrix():
    total_match = 0
    for x in range(1, X_LIMIT-1):
        for y in range(1, Y_LIMIT-1):
            total_match += match(x, y)
    return total_match

print(search_submatrix())
