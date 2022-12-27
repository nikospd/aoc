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
        self.cur_position = (0, 0)
        self.init_state()

    def init_state(self):
        self.direction = 0
        for idx, point in enumerate(self.np_map[0]):
            if point == 1:
                self.cur_position = (0, idx)
                break

    def move(self, steps):
        for step in range(steps):
            next_position, next_direction = self.find_next_position()
            if self.np_map[next_position] == 1:
                self.cur_position = next_position
                self.direction = next_direction
            if self.np_map[next_position] == -1:
                break

    def turn(self, direction):
        if direction == "R":
            self.direction += 1
        else:
            self.direction -= 1
        self.direction = self.direction % 4

    def find_next_position(self):
        next_position = (
            self.cur_position[0] + direction_map[self.direction][0],
            self.cur_position[1] + direction_map[self.direction][1]
        )
        next_direction = self.direction
        if not 0 <= next_position[0] < self.height or not 0 <= next_position[1] < self.width or self.np_map[next_position] == 0:
            next_position, next_direction = self.handle_overflow_v2()
        return next_position, next_direction

    def handle_overflow_v1(self):
        if self.direction == 0:
            idx = (self.np_map[self.cur_position[0], :] != 0).argmax(axis=0)
            return (self.cur_position[0], idx), self.direction
        elif self.direction == 1:
            idx = (self.np_map[:, self.cur_position[1]] != 0).argmax(axis=0)
            return (idx, self.cur_position[1]), self.direction
        elif self.direction == 2:
            idx = (self.np_map[self.cur_position[0], :][::-1] != 0).argmax(axis=0)
            return (self.cur_position[0], self.width - idx - 1), self.direction
        elif self.direction == 3:
            idx = (self.np_map[:, self.cur_position[1]][::-1] != 0).argmax(axis=0)
            return (self.height - idx - 1, self.cur_position[1]), self.direction

    def handle_overflow_v2(self):
        if self.direction == 0:
            if 0 <= self.cur_position[0] < 50:
                # No2
                next_direction = 2
                next_position = (49 - self.cur_position[0] + 100, 99)
            elif 50 <= self.cur_position[0] < 100:
                # No 3
                next_direction = 3
                next_position = (49, self.cur_position[0] - 50 + 100)
            elif 100 <= self.cur_position[0] < 150:
                # No 5
                next_direction = 2
                next_position = (49 - self.cur_position[0] + 100, 149)
            elif 150 <= self.cur_position[0] < 200:
                # No 6
                next_direction = 3
                next_position = (149, self.cur_position[0] - 100)
        elif self.direction == 1:
            if 0 <= self.cur_position[1] < 50:
                # No 6
                next_direction = 1
                next_position = (0, self.cur_position[1] + 100)
            elif 50 <= self.cur_position[1] < 100:
                # No 5
                next_direction = 2
                next_position = (self.cur_position[1] - 50 + 150, 49)
            elif 100 <= self.cur_position[1] < 150:
                # No 2
                next_direction = 2
                next_position = (self.cur_position[1] - 100 + 50, 99)
        elif self.direction == 2:
            if 0 <= self.cur_position[0] < 50:
                # No 1
                next_direction = 0
                next_position = (149 - self.cur_position[0], 0)
            elif 50 <= self.cur_position[0] < 100:
                # No 3
                next_direction = 1
                next_position = (100, self.cur_position[0] - 50)
            elif 100 <= self.cur_position[0] < 150:
                # No 4
                next_direction = 0
                next_position = (49 - self.cur_position[0] + 100, 50)
            elif 150 <= self.cur_position[0] < 200:
                # No 6
                next_direction = 1
                next_position = (0, self.cur_position[0] - 150 + 50)
        elif self.direction == 3:
            if 0 <= self.cur_position[1] < 50:
                # No 4
                next_direction = 0
                next_position = (self.cur_position[1] + 50, 50)
            elif 50 <= self.cur_position[1] < 100:
                # No 1
                next_direction = 0
                next_position = (self.cur_position[1] - 50 + 150, 0)
            elif 100 <= self.cur_position[1] < 150:
                # No 2
                next_direction = 3
                next_position = (199, self.cur_position[1] - 100)
        return next_position, next_direction


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
