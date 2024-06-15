def is_safe(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True
def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True
    for c in range(1, m + 1):
        if is_safe(graph, color, v, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = 0
    return False
def graph_coloring(graph, m):
    color = [0] * len(graph)
    if graph_coloring_util(graph, m, color, 0):
        print("Solution exists: Following are the assigned colors:")
        print(color)
    else:
        print("No solution exists")
vertices = int(input("Enter the number of vertices: "))
graph = []
for i in range(vertices):
    row = list(map(int, input(f"Enter the adjacency list for vertex {i+1} (space-separated): ").split()))
    graph.append(row)
m = int(input("Enter the number of colors: "))
graph_coloring(graph, m)