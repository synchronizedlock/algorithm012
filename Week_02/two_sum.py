from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            if dict.get(target - num) is not None:
                return [dict.get(target - num), i]
            dict[num] = i
