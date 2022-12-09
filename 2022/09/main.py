import time
import math


def move_head(h_coords, direction):
    if direction == "R":
        h_coords[0] += 1
    elif direction == "L":
        h_coords[0] -= 1
    elif direction == "U":
        h_coords[1] += 1
    elif direction == "D":
        h_coords[1] -= 1


def follow_knot(t_coords, h_coords):
    if math.dist(t_coords, h_coords) < 2:
        return
    elif t_coords[0] == h_coords[0]:
        t_coords[1] = int((t_coords[1] + h_coords[1]) / 2)
    elif t_coords[1] == h_coords[1]:
        t_coords[0] = int((t_coords[0] + h_coords[0]) / 2)
    elif abs(t_coords[0] - h_coords[0]) == 1:
        t_coords[0] = h_coords[0]
        t_coords[1] = int((t_coords[1] + h_coords[1]) / 2)
    elif abs(t_coords[1] - h_coords[1]) == 1:
        t_coords[1] = h_coords[1]
        t_coords[0] = int((t_coords[0] + h_coords[0]) / 2)
    else:
        t_coords[0] = int((t_coords[0] + h_coords[0]) / 2)
        t_coords[1] = int((t_coords[1] + h_coords[1]) / 2)


if __name__ == "__main__":
    start_time = time.time()
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()
    t_positions = {}
    knots_coords = []
    for i in range(10):
        knots_coords.append([0, 0])
    t_positions[tuple(knots_coords[-1])] = 1
    for move in input_raw:
        direction, steps = move.split(" ")
        for step in range(int(steps)):
            move_head(knots_coords[0], direction)
            for i in range(len(knots_coords) - 1):
                follow_knot(knots_coords[i+1], knots_coords[i])
            t_positions[tuple(knots_coords[-1])] = 1
    print(len(t_positions))
