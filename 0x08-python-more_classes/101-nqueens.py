#!/usr/bin/python3
"""
addresses the n-queens issue
On this N*N chessboard, the N queens 
are arranged so they cannot capture one another.
"""


def check_safe(brd, row, colm):
    """
    Checks if position is safe - meaning no other queen can attack it

    Args:
        board: The current state of the board
        row: the row that is being checked
        col: the column that is being checked
    Return:
        Returns: either True or False
    """
    # checks if queen can be captured
    for x in range(colm):
        if brd[x] is row or abs(brd[x] - row) is abs(x - colm):
            return False
    return True


def check_board(brd, colm):
    """
    backtracks to verify the column's board condition.

    Arguments: board: the board's current state; col: the column that is being checked
    """
    e = len(brd)
    if colm is e:  # if all items have been iterated
        print(str([[c, brd[c]] for c in range(e)]))
        return

    for row in range(e):  # iterate checking if position is safe
        if check_safe(brd, row, colm):
            brd[colm] = row
            check_board(brd, colm + 1)


if __name__ == "__main__":
    """
    program driver
    """
    import sys

    if len(sys.argv) != 2:
        print("usage: nqueens N")
        sys.exit(1)

    e = 0
    try:
        e = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if e < 4:
        print("N must be at least 4")
        sys.exit(1)

    brd = [0 for colm in range(e)]
    check_board(brd, 0)
