import numpy as np
import math

direction_map = [
    [0, 1],  # Right
    [1, 0],  # Down
    [0, -1],  # Left
    [-1, 0],  # Up
]


class Blizzard(object):

    def __init__(self, position, direction, height, width):
        self.cur_position = position
        self.last_position = position
        self.direction = direction
        self.height = height
        self.width = width

    def move(self):
        next_position = (
            self.cur_position[0] + direction_map[self.direction][0],
            self.cur_position[1] + direction_map[self.direction][1]
        )
        if next_position[0] == 0 or next_position[0] == self.height - 1 or next_position[1] == 0 or next_position[1] == self.width - 1:
            next_position = self.handle_overflow()
        self.last_position = self.cur_position
        self.cur_position = next_position
        return self.last_position, self.cur_position

    def handle_overflow(self):
        if self.direction == 0:
            return self.cur_position[0], 1
        elif self.direction == 1:
            return 1, self.cur_position[1]
        elif self.direction == 2:
            return self.cur_position[0], self.width - 2
        elif self.direction == 3:
            return self.height - 2, self.cur_position[1]


class Human(object):
    def __init__(self, position, goal, map_sim):
        self.cur_position = position
        self.goal = goal
        self.ms = map_sim

    def move(self):
        neighbors = self.ms.free_neighbors(self.cur_position)
        if len(neighbors):
            a = [
                math.dist(self.goal, neighbor)
                for neighbor in neighbors
            ]
            self.cur_position = neighbors[a.index(min(a))]


class MapSimulation(object):

    def __init__(self, input_map):
        self.minute = 0
        self.width = max(list(map(len, input_map)))
        self.height = len(input_map)
        self.np_map = np.zeros((self.height, self.width), int)
        self.blizzards = []
        for i, line in enumerate(input_map):
            for j in range(len(line)):
                point = input_map[i][j]
                if point == ".":
                    self.np_map[i, j] = 0
                elif point == "#":
                    self.np_map[i, j] = -1
                elif point == ">":
                    self.np_map[i, j] = 1
                    self.blizzards.append(Blizzard((i, j), 0, self.height, self.width))
                elif point == "v":
                    self.np_map[i, j] = 1
                    self.blizzards.append(Blizzard((i, j), 1, self.height, self.width))
                elif point == "<":
                    self.np_map[i, j] = 1
                    self.blizzards.append(Blizzard((i, j), 2, self.height, self.width))
                else:
                    self.np_map[i, j] = 1
                    self.blizzards.append(Blizzard((i, j), 3, self.height, self.width))
        self.human = Human((0, 1), (self.height - 1, self.width - 2), self)

    def move(self):
        for blizzard in self.blizzards:
            last_position, cur_position = blizzard.move()
            self.np_map[last_position] -= 1
            self.np_map[cur_position] += 1
        self.human.move()
        self.minute += 1

    def free_neighbors(self, position):
        return [
            (position[0] + direction[0], position[1] + direction[1])
            for direction in direction_map
            if self.np_map[position[0] + direction[0], position[1] + direction[1]] == 0
        ]


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()
    ms = MapSimulation(input_raw)
    while 1:
        ms.move()
        if ms.human.cur_position == ms.human.goal:
            print("reached")
            print(ms.minute)  # wrong! 488
            break
