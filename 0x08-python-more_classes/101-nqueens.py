import sys

def is_valid(board, row, col):
    """
    Checks if a queen can be placed at the given position.

    Args:
        board: A list of lists representing the chessboard.
        row: The row index of the target position.
        col: The column index of the target position.

    Returns:
        True if the position is valid, False otherwise.
    """
    for i in range(row):
        # Check for queens in the same column.
        if board[i][col] == 1:
            return False
        # Check for diagonal attacks.
        diagonals = [(-i, j) for i, j in zip(range(1, row + 1), range(col - row, col + row + 1))]
        if (row + col, row - col) in diagonals and board[row + col][row - col] == 1:
            return False
    return True

def solve_n_queens(n):
    """
    Solves the N queens problem using backtracking and optimization.

    Args:
        n: The size of the chessboard.

    Returns:
        A list of lists, where each inner list represents a solution with queen positions.
    """
    solutions = []
    board = [[0] * n for _ in range(n)]

    def backtrack(row):
        """
        Recursive backtracking to find solutions.

        Args:
            row: The current row index to place a queen.
        """
        if row == n:
            solutions.append([j for j, queen in enumerate(row) if queen == 1])
            return

        # Optimize by prioritizing columns with fewer potential conflicts.
        columns = sorted(range(n), key=lambda c: sum(board[i][c] for i in range(row)))
        for col in columns:
            if is_valid(board, row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    solutions = solve_n_queens(n)
    if not solutions:
        print("No solutions found for N =", n)
    else:
        for solution in solutions:
            print(solution)
