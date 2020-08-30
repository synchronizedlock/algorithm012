import bisect


class Leaderboard:
    def __init__(self):
        self.lookup = {}
        self.scores = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.lookup:
            cur_score = self.lookup[playerId]
            self.scores.remove(cur_score)
            score += cur_score
        self.lookup[playerId] = score
        bisect.insort_left(self.scores, score)

    def top(self, K: int) -> int:
        return sum(self.scores[-K:])

    def reset(self, playerId: int) -> None:
        if playerId in self.lookup:
            self.scores.remove(self.lookup[playerId])
            self.lookup.pop(playerId)

    def __str__(self):
        return "{}{}".format(self.lookup, self.scores)
