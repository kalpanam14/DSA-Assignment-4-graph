#**Implement n-Queen’s Problem
def is_safe(board, row, col, N):
    # Check if the current position is safe from attacks

    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens_util(board, col, N, solutions):
    # Base case: All queens are placed, add the solution
    if col == N:
        solution = []
        for i in range(N):
            row = []
            for j in range(N):
                if board[i][j] == 1:
                    row.append('Q')
                else:
                    row.append('.')
            solution.append(''.join(row))
        solutions.append(solution)
        return True

    # Recursive case: Try placing the queen in each row of the current column
    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1  # Place the queen

            # Recur for the next column
            res = solve_n_queens_util(board, col + 1, N, solutions) or res

            # If placing queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    return res

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

N = 4
solutions = solve_n_queens(N)
for solution in solutions:
    for row in solution:
        print(row)
    print()