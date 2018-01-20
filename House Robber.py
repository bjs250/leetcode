class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        e = 0
        for k in nums:
            temp = i
            i = k + e
            e = max(temp, e)
        return max(i,e)
        
