class Solution:
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def is_exit(x, y):
            return ((x == 0 or x == m - 1 or y == 0 or y == n - 1)
                    and (x, y) != (entrance[0], entrance[1]))

        def dfs(x, y, steps):
            if not (0 <= x < m and 0 <= y < n) or maze[x][y] == '+':
                return float('inf')
            if is_exit(x, y):
                return steps

            maze[x][y] = '+'
            min_steps = float('inf')
            for dx, dy in directions:  # 0 -1
                nx, ny = x + dx, y + dy  #1 1
                min_steps = min(min_steps, dfs(nx, ny, steps + 1))
            maze[x][y] = '.'
            return min_steps

        result = dfs(entrance[0], entrance[1], 0)
        return result if result != float('inf') else -1

maze = []
for _ in range(int(input("Enter the number of rows: "))):
    row = list(input(f"Enter row {_ + 1} (space-separated): ").split())
    maze.append(row)

entrance = list(map(int, input("Enter the entrance coordinates (x y): ").split()))

sol = Solution()
print(sol.nearestExit(maze, entrance))