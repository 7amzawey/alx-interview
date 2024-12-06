#!/usr/bin/python3
"""Place N non-attacking queens on NxN chessboard."""
import sys
from typing import List


def nqueens(n: int) -> List[List[int]]:
    """Solve the nqueen problem with recursive backtracking."""
    cols = set()
    posDiag = set()
    negDiag = set()
    result = []
    solution: List[List[int]] = []

    def backtrack(r):
        """Backtrack funciton."""
        if r == n:
            result.append(solution.copy())
            return
        for c in range(n):
            if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                continue
            cols.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            solution.append([r, c])

            backtrack(r + 1)

            cols.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            solution.pop()
    backtrack(0)
    return result


if __name__ == "__main__":
    """print the solution."""
    n = int(sys.argv[1])
    solutions = nqueens(n)
    for solution in solutions:
        print(solution)
