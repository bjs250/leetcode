class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for n in nums:
            try:
                d[n] += 1
                return True
            except:
                d[n] = 1
        return False
