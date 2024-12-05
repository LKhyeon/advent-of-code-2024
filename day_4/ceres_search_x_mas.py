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

# http://motion.pratt.duke.edu/RoboticSystems/CoordinateTransformations.html
# https://math.stackexchange.com/questions/1676441/how-to-rotate-the-positions-of-a-matrix-by-90-degrees
def rotate_matrix_cw(matrix):
    # Reverse
    flipped = []
    for x in range(len(matrix)):
        row = []
        for y in reversed(range(len(matrix[0]))):
            row.append(matrix[x][y])
        flipped.append(row)

    # Transpose
    transposed = []
    for y in range(len(flipped[0])):
        row = []
        for x in range(len(flipped)):
            row.append(flipped[x][y])
        transposed.append(row)
    
    return transposed

def match(x, y):
    matched_one = False

    rotated = SEARCH_MATRIX_1
    for i in range(4):
        center = MATRIX[y][x] == rotated[1][1]
        north_east = MATRIX[y-1][x+1] == rotated[2][0]
        south_east = MATRIX[y+1][x+1] == rotated[2][2]
        south_west = MATRIX[y+1][x-1] == rotated[0][2]
        north_west = MATRIX[y-1][x-1] == rotated[0][0]
        matched_one = matched_one or (center and north_east and south_east and south_west and north_west)

        rotated = rotate_matrix_cw(rotated)
        
    return int(matched_one)

def search_submatrix():
    total_match = 0
    for x in range(1, X_LIMIT-1):
        for y in range(1, Y_LIMIT-1):
            total_match += match(x, y)
    return total_match

print(search_submatrix())
