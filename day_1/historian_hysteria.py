from pathlib import Path
import re

FILE_PATH = Path(__file__).parent / './test_input.txt'

def parse_text_file():
    arr_1, arr_2 = [], []
    with open(FILE_PATH) as f: 
        for row in f:
            distances = re.split(r'\s+', row)
            arr_1.append(int(distances[0]))
            arr_2.append(int(distances[1]))
    return(arr_1, arr_2)

def compare(arr_1, arr_2):
    arr_1.sort()
    arr_2.sort()

    total_dist = 0
    for i in range(len(arr_1)):
        total_dist += abs(arr_1[i] - arr_2[i])
    return total_dist

def similarity(arr_1, arr_2):
    dist_count = {}
    for dist in arr_2:
        if dist not in dist_count: dist_count[dist] = 0
        dist_count[dist] += 1
    
    total_similarity = 0
    for dist in arr_1:
        if dist in dist_count: total_similarity += dist * dist_count[dist]
    return total_similarity

# Execution:
arr_1, arr_2 = parse_text_file()
print(compare(arr_1, arr_2))
print(similarity(arr_1, arr_2))

