import collections


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        visited = set()
        queue = collections.deque([(word1, word2, 0)])

        while True:
            w1, w2, d = queue.popleft()
            if (w1, w2) not in visited:
                if w1 == w2:
                    return d
                visited.add((w1, w2))
                while w1 and w2 and w1[0] == w2[0]:
                    w1 = w1[1:]
                    w2 = w2[1:]
                d += 1
                queue.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d), (w1[1:], w2, d)])
