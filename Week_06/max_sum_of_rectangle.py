from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        max_k = float("-inf")

        for l in range(len(matrix[0])):
            dp = [0] * len(matrix)
            for r in range(l, len(matrix[0])):
                for i in range(len(matrix)):
                    dp[i] += matrix[i][r]
                sum_dp = 0
                max_dp = float("-inf")
                for d in dp:
                    if sum_dp > 0:
                        sum_dp += d
                    else:
                        sum_dp = d
                    if sum_dp > max_dp:
                        max_dp = sum_dp
                if max_dp <= k:
                    max_k = max(max_k, max_dp)
                    continue
                for t in range(len(dp)):
                    sum_dp = 0
                    for b in range(t, len(dp)):
                        sum_dp += dp[b]
                        if max_k < sum_dp <= k:
                            max_k = sum_dp
                            if max_k == k:
                                return k

        return max_k
