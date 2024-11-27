#!/usr/bin/python3
"""Place N non-attacking queens on NxN chessboard."""
import sys
from typing import List


def nqueens(n: int) -> List[List[int]]:
    """Solve the nqueen problem with recursive backtracking."""
    n = int(sys.argv[0])
    