import collections
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = collections.deque()
        q.append([start, start, 0])
        while q:
            prev, cur, steps = q.popleft()
            if cur == end:
                return steps
            for b in bank:
                if b != prev and sum([s1 != s2 for s1, s2 in zip(b, cur)]) == 1:
                    q.append([cur, b, steps + 1])
        return -1
