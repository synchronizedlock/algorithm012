from functools import reduce
from itertools import combinations


class Solution:
    @staticmethod
    def lib_combine(n, k):
        return list(combinations(range(1, n + 1), k))

    @staticmethod
    def iterative_combine(n, k):
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n + 1)]
        return combs

    @staticmethod
    def reduce_combine(n, k):
        return reduce(lambda two_d_array, _: [[i] + c for c in two_d_array for i in range(1, c[0] if c else n + 1)],
                      range(k), [[]])

    def recursive_combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n + 1) for pre in self.recursive_combine(i - 1, k - 1)]
