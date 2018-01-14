class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        d = {}
        for i in range(1,n+1):
            d[i] = i
        for i in nums:
            try:
                d.pop(i)
            except:
                continue
        return d.keys()


s = Solution()
nums = [1,1]
print s.findDisappearedNumbers(nums)
