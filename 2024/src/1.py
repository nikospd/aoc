from utils import read_input
from pathlib import Path

def get_sides(lines):
    left = []
    right = []
    for line in lines:
        l, r = line.split("   ")
        left.append(l)
        right.append(r)
    left.sort()
    right.sort()
    return left, right

def calculate_distance(left, right):
    distance = 0
    for i in range(len(left)):
        distance += abs(int(right[i]) - int(left[i]))
    return distance

def similarity(left, right):
    frequency = {}
    for item in right:
        frequency[item] = frequency.get(item, 0) + 1
    sum = 0
    for item in left:
        sum += int(item) * frequency.get(item, 0)
    return sum


if __name__ == "__main__":
    lines = read_input(Path(__file__).stem, False)
    # print(calculate_distance(*get_sides(lines)))
    print(similarity(*get_sides(lines)))
