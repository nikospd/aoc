import numpy as np
import re

direction_map = [
    [0, 1],  # Right
    [1, 0],  # Down
    [0, -1],  # Left
    [-1, 0],  # Up
]


class MapSimulation(object):

    def __init__(self, input_map):
        self.width = max(list(map(len, input_map)))
        self.height = len(input_map)
        self.np_map = np.zeros((self.height, self.width), int)
        for i, line in enumerate(input_map):
            for j in range(len(line)):
                point = input_map[i][j]
                if point == ".":
                    self.np_map[i, j] = 1
                if point == "#":
                    self.np_map[i, j] = -1
        self.direction = 0
        for idx, point in enumerate(self.np_map[0]):
            if point == 1:
                self.cur_position = [0, idx]
                break

    def move(self, steps):
        for step in range(steps):
            next_position = self.find_next_position()
            if self.np_map[next_position] == 1:
                self.cur_position = next_position
            if self.np_map[next_position] == -1:
                break

    def turn(self, direction):
        if direction == "R":
            self.direction += 1
        else:
            self.direction -= 1
        self.direction = self.direction % 4

    def find_next_position(self):
        next_position = add_ar(self.cur_position, direction_map[self.direction], self.height, self.width)
        if self.np_map[next_position] == 0:
            if self.direction == 0:
                idx = (self.np_map[self.cur_position[0], :] != 0).argmax(axis=0)
                return self.cur_position[0], idx
            elif self.direction == 1:
                idx = (self.np_map[:, self.cur_position[1]] != 0).argmax(axis=0)
                return idx, self.cur_position[1]
            elif self.direction == 2:
                idx = (self.np_map[self.cur_position[0], :][::-1] != 0).argmax(axis=0)
                return self.cur_position[0], self.width - idx - 1
            elif self.direction == 3:
                idx = (self.np_map[:, self.cur_position[1]][::-1] != 0).argmax(axis=0)
                return self.height - idx - 1, self.cur_position[1]
        return next_position


def add_ar(ar1, ar2, max_height, max_width):
    return (ar1[0] + ar2[0]) % max_height, (ar1[1] + ar2[1]) % max_width


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()
    input_map = input_raw[:-2]
    input_instructions = re.split('(\d+)', input_raw[-1])[1:-1]
    ms = MapSimulation(input_map)
    for instruction in input_instructions:
        if instruction in ["R", "L"]:
            ms.turn(instruction)
        else:
            ms.move(int(instruction))
    print((ms.cur_position[0] + 1) * 1000 + (ms.cur_position[1] + 1) * 4 + ms.direction)
