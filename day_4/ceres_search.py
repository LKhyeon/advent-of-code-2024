from pathlib import Path
import re

FILE_PATH = Path(__file__).parent / './test_input.txt'

def parse_text_file():
    matrix = []
    with open(FILE_PATH) as f: 
        for row in f:
            matrix.append(list(row.strip()))
    return(matrix)

KEYWORD = 'XMAS'
MATRIX = parse_text_file()

X_LIMIT = len(MATRIX[0])
Y_LIMIT = len(MATRIX)

def search_east(x, y):
    if x + len(KEYWORD) > X_LIMIT: return 0
    
    match = True
    for i in range(len(KEYWORD)):
        if KEYWORD[i] != MATRIX[y][x+i]: match = False
    return int(match)

def search_north_east(x, y):
    if x + len(KEYWORD) > X_LIMIT: return 0
    if y - len(KEYWORD) + 1 < 0: return 0

    match = True
    for i in range(len(KEYWORD)):
        if KEYWORD[i] != MATRIX[y-i][x+i]: match = False
    return int(match)

def search_north(x, y):
    if y - len(KEYWORD) + 1 < 0: return 0
    
    match = True
    for i in range(len(KEYWORD)):
        if KEYWORD[i] != MATRIX[y-i][x]: match = False
    return int(match)

def search_north_west(x, y):
    if x - len(KEYWORD) + 1 < 0: return 0
    if y - len(KEYWORD) + 1 < 0: return 0

    match = True
    for i in range(len(KEYWORD)):
        if KEYWORD[i] != MATRIX[y-i][x-i]: match = False
    return int(match)

def search_west(x, y):
    if x - len(KEYWORD) + 1 < 0: return 0
    
    match = True
    for i in range(len(KEYWORD)):
        if KEYWORD[i] != MATRIX[y][x-i]: match = False
    return int(match)

def search_south_west(x, y):
    if x - len(KEYWORD) + 1 < 0: return 0
    if y + len(KEYWORD) > Y_LIMIT: return 0

    match = True
    for i in range(len(KEYWORD)):
        if KEYWORD[i] != MATRIX[y+i][x-i]: match = False
    return int(match)

def search_south(x, y):
    if y + len(KEYWORD) > Y_LIMIT: return 0
    
    match = True
    for i in range(len(KEYWORD)):
        if KEYWORD[i] != MATRIX[y+i][x]: match = False
    return int(match)

def search_south_east(x, y):
    if x + len(KEYWORD) > X_LIMIT: return 0
    if y + len(KEYWORD) > Y_LIMIT: return 0

    match = True
    for i in range(len(KEYWORD)):
        if KEYWORD[i] != MATRIX[y+i][x+i]: match = False
    return int(match)

def search_keyword():
    total_match = 0
    for x in range(X_LIMIT):
        for y in range(Y_LIMIT):
            total_match += search_east(x, y)
            total_match += search_north_east(x, y)
            total_match += search_north(x, y)
            total_match += search_north_west(x, y)
            total_match += search_west(x, y)
            total_match += search_south_west(x, y)
            total_match += search_south(x, y)
            total_match += search_south_east(x, y)
    
    return total_match

print(search_keyword())
