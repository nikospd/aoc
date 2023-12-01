import numpy as np
import math
import time


def find_dimensions(matrix):
    return max([row[0] for row in matrix]), max([row[1] for row in matrix]), max([row[2] for row in matrix])


def get_surface_area(matrix):
    surface = 6
    if len(matrix) == 1:
        return surface
    for i in range(1, len(matrix)):
        new_surface = 6
        for j in range(i):
            if math.dist(matrix[i], matrix[j]) == 1:
                new_surface -= 2
        surface += new_surface
    return surface


def floodFill(x, y, z, matrix, dimensions):
    if not 0 < x <= dimensions[0]:
        return
    if not 0 < y <= dimensions[1]:
        return
    if not 0 < z <= dimensions[2]:
        return
    if [x, y, z] in matrix:
        return
    matrix.append([x, y, z])
    floodFill(x + 1, y, z, matrix, dimensions)
    floodFill(x - 1, y, z, matrix, dimensions)
    floodFill(x, y + 1, z, matrix, dimensions)
    floodFill(x, y - 1, z, matrix, dimensions)
    floodFill(x, y, z + 1, matrix, dimensions)
    floodFill(x, y, z - 1, matrix, dimensions)


def isValid(x, y, z, matrix, dimensions):
    if not 0 < x <= dimensions[0]:
        return False
    if not 0 < y <= dimensions[1]:
        return False
    if not 0 < z <= dimensions[2]:
        return False
    if [x, y, z] in matrix:
        return False
    return True


def floodFillQueue(x, y, z, matrix, dimensions):
    queue = [[x, y, z]]
    matrix.append([x, y, z])

    while queue:
        cur_point = queue.pop()
        if isValid(cur_point[0] + 1, cur_point[1], cur_point[2], matrix, dimensions):
            queue.append([cur_point[0] + 1, cur_point[1], cur_point[2]])
            matrix.append([cur_point[0] + 1, cur_point[1], cur_point[2]])
        if isValid(cur_point[0] - 1, cur_point[1], cur_point[2], matrix, dimensions):
            queue.append([cur_point[0] - 1, cur_point[1], cur_point[2]])
            matrix.append([cur_point[0] - 1, cur_point[1], cur_point[2]])
        if isValid(cur_point[0], cur_point[1] + 1, cur_point[2], matrix, dimensions):
            queue.append([cur_point[0], cur_point[1] + 1, cur_point[2]])
            matrix.append([cur_point[0], cur_point[1] + 1, cur_point[2]])
        if isValid(cur_point[0], cur_point[1] - 1, cur_point[2], matrix, dimensions):
            queue.append([cur_point[0], cur_point[1] - 1, cur_point[2]])
            matrix.append([cur_point[0], cur_point[1] - 1, cur_point[2]])
        if isValid(cur_point[0], cur_point[1], cur_point[2] + 1, matrix, dimensions):
            queue.append([cur_point[0], cur_point[1], cur_point[2] + 1])
            matrix.append([cur_point[0], cur_point[1], cur_point[2] + 1])
        if isValid(cur_point[0], cur_point[1], cur_point[2] - 1, matrix, dimensions):
            queue.append([cur_point[0], cur_point[1], cur_point[2] - 1])
            matrix.append([cur_point[0], cur_point[1], cur_point[2] - 1])


if __name__ == "__main__":
    start_time = time.time()
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()

    drops = []
    for line in input_raw:
        drops.append(list(map(int, line.split(","))))

    drops_surface = get_surface_area(drops)
    print("drops: ", drops_surface)

    dimensions = find_dimensions(drops)
    # floodFill(1, 1, 1, drops, dimensions)
    floodFillQueue(1, 1, 1, drops, dimensions)

    trapped = []
    for i in range(1, dimensions[0]):
        for j in range(1, dimensions[1]):
            for z in range(1, dimensions[2]):
                if [i, j, z] not in drops:
                    trapped.append([i, j, z])
    trapped_surface = get_surface_area(trapped)
    print("trapped: ", trapped_surface)
    print("w/out trapped: ", drops_surface - trapped_surface)
    print("--- %s seconds ---" % (time.time() - start_time))

