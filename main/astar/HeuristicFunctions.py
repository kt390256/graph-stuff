# -*- coding: utf-8 -*-

# can move in 4 directions
def manhattan(start, end):
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    D = 1       # cost to move adjacent
    return D * (dx + dy)

# can move diagonally
def chebyshev(start, end):
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    D = 1       # cost to move adjacent
    D2 = D * 2  # cost to move diagonally
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
