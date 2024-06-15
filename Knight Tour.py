N = int(input("Enter the size of the board: "))
knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)]
def is_safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1
def print_board(board):
    for row in board:
        print(' '.join(str(cell).zfill(2) for cell in row))
    print()
def solve_knight_tour():
    board = [[-1 for _ in range(N)] for _ in range(N)]
    start_x, start_y = 0, 0
    board[start_x][start_y] = 0
    if not solve_knight_tour_util(board, start_x, start_y, 1):
        print("No solution exists")
    else:
        print_board(board)
def solve_knight_tour_util(board, curr_x, curr_y, move_count):
    if move_count == N * N:
        return True
    for move in knight_moves: 
        next_x, next_y = curr_x + move[0], curr_y + move[1]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = move_count
            if solve_knight_tour_util(board, next_x, next_y, move_count + 1):
                return True
            board[next_x][next_y] = -1
    return False
solve_knight_tour()