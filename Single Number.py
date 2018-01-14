class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for i in nums:
            try:
                d.pop(i)
            except:
                d[i] = 1
        return d.popitem()[0]

s = Solution()
nums = [1, 2, 3, 4, 3, 1, 2]
print s.singleNumber(nums)
