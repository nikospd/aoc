import numpy as np
import copy


def create_cave(input_raw):
    cave_map = np.zeros((200, 700), int)
    max_height = 0
    for line in input_raw:
        points = line.split(" -> ")
        for i in range(len(points) - 1):
            x1, y1 = list(map(int, points[i].split(",")))  # 498, 4
            x2, y2 = list(map(int, points[i + 1].split(",")))  # 498, 6
            if max(y1, y2) > max_height:
                max_height = max(y1, y2)
            if x1 == x2:
                if y2 > y1:
                    for j in range(y1, y2 + 1):
                        cave_map[j][x1] = 1
                elif y2 < y1:
                    for j in range(y2, y1 + 1):
                        cave_map[j][x1] = 1
                else:
                    print("here1")
            if y1 == y2:
                if x2 > x1:
                    for j in range(x1, x2 + 1):
                        cave_map[y2][j] = 1
                elif x2 < x1:
                    for j in range(x2, x1 + 1):
                        cave_map[y2][j] = 1
                else:
                    print("here2")
    for i in range(cave_map.shape[1]):
        cave_map[max_height + 2][i] = 1
    return cave_map, max_height


def sand_simulation_v1(cave_map, max_height, starting_point):
    units = 0
    while 1:
        sand = copy.deepcopy(starting_point)
        while 1:
            if sand[0] + 1 == max_height + 2:
                return units
            if cave_map[sand[0] + 1][sand[1]] == 0:
                sand[0] = sand[0] + 1
            elif cave_map[sand[0] + 1][sand[1] - 1] == 0:
                sand[0] = sand[0] + 1
                sand[1] = sand[1] - 1
            elif cave_map[sand[0] + 1][sand[1] + 1] == 0:
                sand[0] = sand[0] + 1
                sand[1] = sand[1] + 1
            else:
                units += 1
                cave_map[sand[0]][sand[1]] = 2
                break


def sand_simulation_v2(cave_map, starting_point):
    units = 0
    while 1:
        sand = copy.deepcopy(starting_point)
        while 1:
            if cave_map[sand[0] + 1][sand[1]] == 0:
                sand[0] = sand[0] + 1
            elif cave_map[sand[0] + 1][sand[1] - 1] == 0:
                sand[0] = sand[0] + 1
                sand[1] = sand[1] - 1
            elif cave_map[sand[0] + 1][sand[1] + 1] == 0:
                sand[0] = sand[0] + 1
                sand[1] = sand[1] + 1
            else:
                if sand == starting_point:
                    return units + 1
                units += 1
                cave_map[sand[0]][sand[1]] = 2
                break


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()

    cave_map, max_height = create_cave(input_raw)

    starting_point = [0, 500]
    # rested_units = sand_simulation_v1(cave_map, max_height, starting_point)
    rested_units = sand_simulation_v2(cave_map, starting_point)
    print(rested_units)
