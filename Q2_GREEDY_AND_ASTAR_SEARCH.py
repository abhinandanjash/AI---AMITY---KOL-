"""
EXPERIMENT 2: GREEDY BEST-FIRST SEARCH AND A* SEARCH
"""

import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('E', 3)],
    'E': []
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 0
}


def greedy_best_first(start, goal):
    pq = [(heuristic[start], start, [start])]
    visited = set()

    while pq:
        h, node, path = heapq.heappop(pq)

        if node == goal:
            print("Greedy Path:", path)
            return

        if node in visited:
            continue
        visited.add(node)

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(
                    pq,
                    (heuristic[neighbour], neighbour, path + [neighbour])
                )

    print("Path not found")


def a_star(start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if g != best_cost.get(node):
            continue

        if node == goal:
            print("A* Path:", path)
            print("Total Cost:", g)
            return

        for neighbour, cost in graph[node]:
            new_cost = g + cost
            if new_cost < best_cost.get(neighbour, float('inf')):
                best_cost[neighbour] = new_cost
                heapq.heappush(
                    pq,
                    (new_cost + heuristic[neighbour], new_cost, neighbour, path + [neighbour])
                )

    print("Path not found")


if __name__ == "__main__":
    print("=== EXPERIMENT 2: GREEDY BEST-FIRST & A* SEARCH ===")
    greedy_best_first('A', 'E')
    a_star('A', 'E')
