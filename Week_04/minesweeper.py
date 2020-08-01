import itertools
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        a, b = click
        if board[a][b] == 'M':
            board[a][b] = 'X'
        elif board[a][b] == 'E':
            d = [*itertools.product((-1, 0, 1), repeat=2)]
            q, v, m, n = [(a, b)], {(a, b)}, len(board), len(board[0])
            while q:
                p = []
                for i, j in q:
                    c, t = 0, []
                    for di, dj in d:
                        x, y = i + di, j + dj
                        if 0 <= x < m and 0 <= y < n:
                            c += board[x][y] == 'M'
                            (x, y) not in v and t.append((x, y))
                    board[i][j] = c and str(c) or p.extend(t) or v.update(t) or 'B'
                q = p
        return board
