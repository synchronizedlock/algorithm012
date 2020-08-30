from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        import bisect
        arr = []
        res = 0
        for num in nums:
            res += len(arr) - bisect.bisect_right(arr, num * 2)
            loc = bisect.bisect_right(arr, num)
            arr[loc:loc] = [num]
        return res
