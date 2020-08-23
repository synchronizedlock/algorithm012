from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set([str(i) for i in range(1, 10)]) for j in range(1, 10)]
        cols = [set([str(i) for i in range(1, 10)]) for j in range(1, 10)]
        blocks = [set([str(i) for i in range(1, 10)]) for j in range(1, 10)]
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append([i, j])
                else:
                    rows[i].remove(board[i][j])
                    cols[j].remove(board[i][j])
                    b = (i // 3) * 3 + (j // 3)
                    blocks[b].remove(board[i][j])

        def check(index):
            if index >= len(empty):
                return True
            i, j = empty[index]
            b = (i // 3) * 3 + (j // 3)
            for key in rows[i] & cols[j] & blocks[b]:

                rows[i].remove(key)
                cols[j].remove(key)
                blocks[b].remove(key)
                board[i][j] = key
                if check(index + 1):
                    return True
                rows[i].add(key)
                cols[j].add(key)
                blocks[b].add(key)
            return False

        return check(0)
