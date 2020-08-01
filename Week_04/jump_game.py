from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == [0]:
            return True
        max_dist = 0
        end_index = len(nums) - 1
        for i, jump in enumerate(nums):
            if i <= max_dist < i + jump:
                max_dist = i + jump
                if max_dist >= end_index:
                    return True
        return False
