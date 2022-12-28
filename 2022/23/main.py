import numpy as np

north = (-1, 0)
north_east = (-1, 1)
north_west = (-1, -1)

south = (1, 0)
south_east = (1, 1)
south_west = (1, -1)

west = (0, -1)
east = (0, 1)

proposes = [
    [north, [north, north_east, north_west]],  # Moving North
    [south, [south, south_east, south_west]],  # Moving South
    [west, [west, north_west, south_west]],  # Moving West
    [east, [east, north_east, south_east]],  # Moving East
]

offset = 80


class ElfMapSimulation(object):
    def __init__(self, input_map):
        self._height = len(input_map) + 2 * offset
        self._width = len(input_map[0]) + 2 * offset
        self._map = np.zeros((self._height, self._width), int)
        self._proposes_dict = {}
        self._nof = 0
        self.init_state(input_map)

    def init_state(self, input_map):
        for i, line in enumerate(input_map):
            for j, tile in enumerate(line):
                if tile == "#":
                    self._map[i + offset][j + offset] = 1
                    self._nof += 1

    def move(self):
        if not len(self._proposes_dict):
            return False
        self._proposes_dict = {
            key: value
            for key, value in self._proposes_dict.items()
            if list(self._proposes_dict.values()).count(value) == 1
        }
        for key, value in self._proposes_dict.items():
            self._map[key] = 0
            self._map[value] = 1
        self._proposes_dict = {}
        proposes.append(proposes.pop(0))
        return True

    def propose(self):
        for ix, line in enumerate(self._map):
            for iy, tile in enumerate(line):
                if tile:
                    proposes_res = [
                        self.evaluate_propose((ix, iy), propose[1])
                        for propose in proposes
                    ]
                    if all(proposes_res):
                        continue
                    if not any(proposes_res):
                        continue
                    idx = proposes_res.index(True)
                    self._proposes_dict[(ix, iy)] = find_next((ix, iy), proposes[idx][0])

    def evaluate_propose(self, position, propose):
        for direction in propose:
            if self._map[position[0] + direction[0]][position[1] + direction[1]]:
                return False
        return True

    def progress(self):
        max_hor = 0
        min_hor = self._width
        for i in range(self._height):
            if 1 in self._map[i, :]:
                min_hor = min(min_hor, (self._map[i, :] == 1).argmax(axis=0))
                max_hor = max(max_hor, self._width - (self._map[i, :][::-1] == 1).argmax(axis=0))

        max_ver = 0
        min_ver = self._height
        for i in range(self._width):
            if 1 in self._map[:, i]:
                min_ver = min(min_ver, (self._map[:, i] == 1).argmax(axis=0))
                max_ver = max(max_ver, self._height - (self._map[:, i][::-1] == 1).argmax(axis=0))

        return (max_hor - min_hor) * (max_ver - min_ver) - self._nof

    def run(self):
        for _ in range(10):
            self.propose()
            self.move()
        print(self.progress())

    def run_v2(self):
        rounds = 1
        while 1:
            self.propose()
            if not self.move():
                print(rounds)
                break
            rounds += 1



def find_length(arr):
    return len("".join(map(str, arr)).lstrip("0").rstrip("0"))


def find_next(position, direction):
    return position[0] + direction[0], position[1] + direction[1]


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()

    ems = ElfMapSimulation(input_raw)

    # ems.run()
    ems.run_v2()
