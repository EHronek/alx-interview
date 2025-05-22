#!/usr/bin/python3
"""Defines an algorithm that Solves the N Queens problem using backtracking."""
import sys


def is_safe(board, row, col):
    """Function checkss if placing a queen at (row, col) is safe."""
    for ro in range(row):
        c = board[ro]
        if c == col or abs(c - col) == abs(ro - row):
            return False
    return True


def solve_nqueens(n, row=0, board=[], solutions=[]):
    """Function recursively solvse the N Queens problem using backtracking."""
    if row == n:
        solution = [[r, board[r]] for r in range(n)]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueens(n, row + 1, board, solutions)
            board.pop()


def main():
    """Main entry point for the script. Handles input and prints solutions."""
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
    solve_nqueens(n, 0, [], solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
