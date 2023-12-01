import numpy as np
from collections import deque
from heapq import *

def find_neighbors(map, x, y):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        neighbor = (x + dir[0], y + dir[1])
        if 0 <= neighbor[0] < map.shape[0] and 0 <= neighbor[1] < map.shape[1]:
            if abs(map[x, y] - map[neighbor[0], neighbor[1]]) <= 1:
                result.append((1,neighbor))
    return result

def next_node(neighbors_map, current_node, finish_node):
    if finish_node == current_node:
        return [finish_node]
    for neighbors in neighbors_map[current_node]:
        tmp = next_node(neighbors_map, neighbors, finish_node)
        tmp.append(current_node)
        return tmp

def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break
        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return visited

def dijkstra(start, goal, graph):
    queue = []
    heappush(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    return visited

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()
    starting_point = (0, 0)
    ending_point = (2, 5)

    map = np.zeros((len(input_raw), len(input_raw[0])), np.int16)
    for i1 in range(len(input_raw)):
        for j1 in range(len(input_raw[i1])):
            map[i1][j1] = ord(input_raw[i1][j1]) - 96
            if map[i1][j1] == -13:
                starting_point = (i1, j1)
                map[i1][j1] = 1
            if map[i1][j1] == -27:
                ending_point = (i1, j1)
                map[i1][j1] = 26

    neighbors_map = {}
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            neighbors_map[(i, j)] = (find_neighbors(map, i, j))
    # ending_point = (2,0)


    visited = dijkstra(starting_point, ending_point, neighbors_map)
    # visited = bfs(starting_point, ending_point, neighbors_map)

    cur_node = ending_point
    num = 0
    while cur_node != starting_point:
        num+=1
        cur_node = visited[cur_node]
        print(f'---> {cur_node}', end='')

    print("dsa")