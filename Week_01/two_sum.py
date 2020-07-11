class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in num_dict:
                return [num_dict[another_num], index]
            num_dict[num] = index
        return None
