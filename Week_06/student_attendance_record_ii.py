class Solution(object):
    def checkRecord(self, n):
        M = 10 ** 9 + 7
        a, b, c, d, e, f = [1, 1, 0, 1, 0, 0]
        for i in range(n):
            a, b, c = (a + b + c) % M, a, b
            d, e, f = (a + d + e + f) % M, d, e
        return d
