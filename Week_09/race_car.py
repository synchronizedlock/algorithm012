class Solution:
    def racecar(self, target: int) -> int:
        def race(t):
            if t not in dp:
                n = t.bit_length()
                if (1 << n) - 1 == t:
                    dp[t] = n
                else:
                    dp[t] = n + 1 + race((1 << n) - 1 - t)
                    for m in range(n - 1):
                        dp[t] = min(dp[t], n + m + 1 + race(t - (1 << n - 1) + (1 << m)))
            return dp[t]

        dp = {0: 0}
        return race(target)
