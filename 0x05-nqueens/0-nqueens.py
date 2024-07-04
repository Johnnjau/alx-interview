#!/usr/bin/python3
"""
0. N queens
"""
import sys


def nqueens_backtrack(n, y, board):
    """
    ngqueens backtracking function
    """
    for r in range(n):
        current = 0
        for c in board:
            # wether current position is valid for a queen
            if r == c[1] or abs(r - c[1]) == abs(y - c[0]):
                current = 1
                break
        if current == 0:
            board.append([y, r])
            if y == n - 1:
                # If at last row, print board
                print(board)
            else:
                # move to next row
                nqueens_backtrack(n, y + 1, board)
            board.pop()


def nqueens(n):
    """
    nqueens problem with NxN board
    """
    board = []
    nqueens_backtrack(n, 0, board)


def main():
    """
    entry point and handel sys args
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(n)


if __name__ == "__main__":
    main()
