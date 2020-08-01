from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        loc = [0, 0]
        deg = 90
        ans = 0
        obstacles_set = set(map(tuple, obstacles))
        for num in commands:
            if num == -1:
                deg = (deg + 270) % 360
            elif num == -2:
                deg = (deg + 90) % 360
            else:
                if deg == 0:
                    i = 0
                    while i < num and not (loc[0] + 1, loc[1]) in obstacles_set:
                        loc[0] += 1
                        i += 1
                if deg == 90:
                    i = 0
                    while i < num and not (loc[0], loc[1] + 1) in obstacles_set:
                        loc[1] += 1
                        i += 1
                if deg == 180:
                    i = 0
                    while i < num and not (loc[0] - 1, loc[1]) in obstacles_set:
                        loc[0] -= 1
                        i += 1
                if deg == 270:
                    i = 0
                    while i < num and not (loc[0], loc[1] - 1) in obstacles_set:
                        loc[1] -= 1
                        i += 1
                ans = max(ans, loc[0] ** 2 + loc[1] ** 2)
        return ans
