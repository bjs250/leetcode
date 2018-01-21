class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = list()
        for i in range(len(nums)+1):
            L.append(0)
        for n in nums:
            L[n] = 1
        for index, element in enumerate(L):
            if element == 0:
                return index

sol = Solution()
nums = [3, 0, 1]
print(sol.missingNumber(nums))
