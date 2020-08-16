from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def test_mid(mid):
            s, num = 0, 1

            for i in nums:
                if s + i > mid:
                    s = i
                    num += 1
                else:
                    s += i

            return num > m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if_right = test_mid(mid)
            if if_right:
                left = mid + 1
            else:
                right = mid

        return left
