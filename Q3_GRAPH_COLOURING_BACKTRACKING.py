"""
EXPERIMENT 3: GRAPH COLOURING USING BACKTRACKING
"""

V = 4
adj_matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
colors = ['Red', 'Green', 'Blue']
result = [None] * V


def is_safe(vertex, color):
    for i in range(V):
        if adj_matrix[vertex][i] == 1 and result[i] == color:
            return False
    return True


def graph_coloring(vertex):
    if vertex == V:
        return True

    for color in colors:
        if is_safe(vertex, color):
            result[vertex] = color
            if graph_coloring(vertex + 1):
                return True
            result[vertex] = None

    return False


if __name__ == "__main__":
    print("=== EXPERIMENT 3: GRAPH COLOURING USING BACKTRACKING ===")
    if graph_coloring(0):
        print("Graph Coloring Solution:")
        for i in range(V):
            print("Vertex", i, ":", result[i])
    else:
        print("No solution exists.")
