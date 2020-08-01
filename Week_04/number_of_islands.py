from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        point_to_island = {}
        island_to_point = {}

        for line in range(len(grid)):
            for col in range(len(grid[0])):
                flag = False
                if grid[line][col] == '1':
                    if line > 0 and grid[line - 1][col] == '1':
                        island_left = point_to_island[(line - 1, col)]
                        point_to_island[(line, col)] = island_left
                        island_to_point[island_left].append((line, col))
                        flag = True

                    if col > 0 and grid[line][col - 1] == '1':
                        island_top = point_to_island[(line, col - 1)]
                        if flag and island_top != island_left:
                            self.combine_island(island_top, island_left, point_to_island, island_to_point)
                        elif flag:
                            continue
                        else:
                            point_to_island[(line, col)] = island_top
                            island_to_point[island_top].append((line, col))
                        flag = True

                    if flag:
                        continue
                    else:
                        point_to_island[(line, col)] = (line, col)
                        island_to_point[(line, col)] = [(line, col)]
        return len(island_to_point)

    def combine_island(self, island_top, island_left, point_to_island, island_to_point):
        island_top_part = island_to_point[island_top]
        island_left_part = island_to_point[island_left]
        if len(island_top_part) > len(island_left_part):
            for point in island_left_part:
                point_to_island[point] = island_top
            island_to_point[island_top].extend(island_left_part)
            del island_to_point[island_left]
        else:
            for point in island_top_part:
                point_to_island[point] = island_left
            island_to_point[island_left].extend(island_top_part)
            del island_to_point[island_top]
