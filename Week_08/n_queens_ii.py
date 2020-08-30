class Solution:
    def totalNQueens(self, n: int) -> int:
        def func(i):
            if i == n:
                self.s += 1
            else:
                for j in range(n):
                    if d1[j] and d2[i + j] and d3[i - j]:
                        d1[j], d2[i + j], d3[i - j] = 0, 0, 0
                        func(i + 1)
                        d1[j], d2[i + j], d3[i - j] = 1, 1, 1

        d1, d2, d3, self.s = [1] * n, [1] * (2 * n), [1] * (2 * n), 0
        func(0)
        return self.s
