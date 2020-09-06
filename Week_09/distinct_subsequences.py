import collections


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        slen, tlen = len(s), len(t)
        if slen < tlen:
            return 0
        tdict = collections.defaultdict(list)
        for i, c in enumerate(t):
            tdict[c].append(i)
        dp = [1] + [0] * tlen
        for ch in s:
            for j in tdict[ch][::-1]:
                dp[j + 1] += dp[j]
        return dp[-1]
