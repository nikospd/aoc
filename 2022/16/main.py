import statistics
import string
from parse import parse
from collections import deque
import copy


def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break
        next_nodes = graph[cur_node]["destinations"]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node

    path = []
    cur_node = goal
    while cur_node != start:
        path.insert(0, cur_node)
        cur_node = visited[cur_node]
    return path


if __name__ == "__main__":
    with open("input_test.txt", "r") as file:
        input_raw = file.read().splitlines()
    t1 = "Valve {origin} has flow rate={flow_rate}; tunnels lead to valves {destinations}"
    t2 = "Valve {origin} has flow rate={flow_rate}; tunnel leads to valve {destinations}"
    # Build graph
    graph = {}
    for line in input_raw:
        data = parse(t1, line)
        if not data:
            data = parse(t2, line)
        graph[data["origin"]] = {"flow_rate": int(data["flow_rate"]), "destinations": data["destinations"].split(", ")}

    remaining_valves = {}
    for point in graph:
        if graph[point]["flow_rate"] > 0:
            remaining_valves[point] = graph[point]

    visited = ["AA"]
    last_point = "AA"
    cur_point = "AA"
    # while len(remaining_valves):
    #     for point in graph[cur_point]["destinations"]:
    #         if point not in visited:







    next_point = max(remaining_valves, key=lambda x: remaining_valves[x]["flow_rate"])
    bfs(cur_point, next_point, graph)
    path = bfs(cur_point, next_point, graph)
    for point in path:
        if graph[point]["flow_rate"] > statistics.mean(
            [
                remaining_valves[remaining_point]["flow_rate"]
                for remaining_point in remaining_valves
            ]
        ):
            print("open_valve: ", point)
            remaining_valves.pop(point)
            cur_point = point
            break




    minutes = 30


