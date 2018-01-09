class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if (i != j):
                    val = nums[i]+nums[j]
                    d[str(val)] = [i, j]
        if (str(target) in d):
            return d[str(target)]
        else:
            return None


s = Solution()
print(s.twoSum([5, 6, 7], 11))
