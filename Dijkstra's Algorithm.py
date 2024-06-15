def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()
    while len(visited) < len(graph):
        min_vertex = None
        for vertex in graph:
            if vertex not in visited:
                if min_vertex is None or distances[vertex] < distances[min_vertex]:
                    min_vertex = vertex
        if min_vertex is None:
            break
        for neighbor, weight in graph[min_vertex].items():
            if neighbor not in visited:
                new_distance = distances[min_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
        visited.add(min_vertex)
    return distances
graph_input = input("Enter the graph (key-value pairs separated by a colon, keys separated by commas): ").strip()
graph = {k: {nbr: int(w) for nbr, w in [tuple(x.split()) for x in v.split(',')]} for k, v in [tuple(x.split(':')) for x in graph_input.split(',')]}
start_vertex = input("Enter the starting vertex: ").strip()
distances = dijkstra(graph, start_vertex)
print(distances)