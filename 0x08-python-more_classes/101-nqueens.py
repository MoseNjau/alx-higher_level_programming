#!/usr/bin/python3
import sys

def print_solution(queens):
    solution = []
    for row, col in enumerate(queens):
        solution.append([row, col])
    print(solution)

def is_safe(queens, row, col):
    for r in range(row):
        if queens[r] == col or \
           queens[r] - r == col - row or \
           queens[r] + r == col + row:
            return False
    return True

def solve_n_queens(n, queens, row):
    if row == n:
        print_solution(queens)
        return
    
    for col in range(n):
        if is_safe(queens, row, col):
            queens[row] = col
            solve_n_queens(n, queens, row + 1)

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

    queens = [-1] * n
    solve_n_queens(n, queens, 0)

if __name__ == "__main__":
    main()
