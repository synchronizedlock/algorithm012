import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        return collections.Counter(s) == collections.Counter(t)
