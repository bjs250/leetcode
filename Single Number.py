class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for i in range(len(nums)):
            if str(nums[i]) in d.keys():
                d.pop(str(nums[i]))
            else:
                d[str(nums[i])] = nums[i]
        return int(d.keys()[0])

s = Solution()
nums = [1, 2, 3, 4, 3, 1, 2]
print s.singleNumber(nums)
