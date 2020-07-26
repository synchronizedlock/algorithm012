class Solution:
    def permuteUnique(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    new_perms.append(p[:i] + [n] + p[i:])
                    if i < len(p) and p[i] == n:
                        break
            perms = new_perms
        return perms
