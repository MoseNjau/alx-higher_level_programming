import sys

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, board, row, solutions):
    if row == n:
        solutions.append(board.copy())
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(n, board, row + 1, solutions)

def print_solutions(solutions):
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n
    solve_n_queens(n, board, 0, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
