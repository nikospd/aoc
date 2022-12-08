import numpy as np
import time


def is_visible(tree_row, height):
    if len(tree_row) == 0:
        return True
    if height <= int(tree_row[0]):
        return False
    return is_visible(tree_row[1:], height)


def viewing_distance(tree_row, height):
    if len(tree_row) == 0:
        return 0
    if height <= int(tree_row[0]):
        return 1
    return 1 + viewing_distance(tree_row[1:], height)


def calculate_visible_trees(forest):
    visible_trees = 0
    for i in range(forest.shape[0]):
        for j in range(forest.shape[1]):
            if i == forest.shape[0] - 1 or j == forest.shape[1] - 1:
                visible_trees += 1
            elif is_visible(forest[i, :j][::-1], forest[i, j]) or is_visible(forest[i, j + 1:],
                                                                             forest[i, j]) or is_visible(
                    forest[:i, j][::-1], forest[i, j]) or is_visible(forest[i + 1:, j], forest[i, j]):
                visible_trees += 1
    return visible_trees


def calculate_max_scenic(forest):
    max_scenic = 0
    for i in range(forest.shape[0]):
        for j in range(forest.shape[1]):
            viewing_distance_west = viewing_distance(forest[i, :j][::-1], forest[i, j])
            viewing_distance_east = viewing_distance(forest[i, j + 1:], forest[i, j])
            viewing_distance_north = viewing_distance(forest[:i, j][::-1], forest[i, j])
            viewing_distance_south = viewing_distance(forest[i + 1:, j], forest[i, j])
            scenic = viewing_distance_west * viewing_distance_east * viewing_distance_north * viewing_distance_south
            max_scenic = max(scenic, max_scenic)
    return max_scenic


if __name__ == "__main__":
    start_time = time.time()
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()
    forest = np.zeros((len(input_raw), len(input_raw[0])), np.int16)
    for i in range(len(input_raw)):
        for j in range(len(input_raw[i])):
            forest[i][j] = (int(input_raw[i][j]))

    # print(calculate_visible_trees(forest))

    print(calculate_max_scenic(forest))

    print("--- %s seconds ---" % (time.time() - start_time))
