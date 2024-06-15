def tsp_recursive(distance_matrix):
    n = len(distance_matrix)
    def all_cities_visited(visited):
        return len(visited) == n
    def tsp(visited, pos):
        if all_cities_visited(visited):
            return distance_matrix[pos][0]
        min_distance = float('inf')
        for city in range(n):
            if city not in visited:
                new_visited = visited + [city]
                new_distance = distance_matrix[pos][city] + tsp(new_visited, city)
                min_distance = min(min_distance, new_distance)

        return min_distance

    initial_visited = [0]
    return tsp(initial_visited, 0)

n = int(input("Enter the number of cities: "))

distance_matrix = []
for i in range(n):
    row = input(f"Enter the distances from city {i + 1} to other cities (separated by spaces): ")
    row = list(map(int, row.split()))
    distance_matrix.append(row)

min_distance = tsp_recursive(distance_matrix)
print(f"Minimum distance: {min_distance}")