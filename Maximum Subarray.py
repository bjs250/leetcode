class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curSum = list()
        curSum.append(nums[0])
        for num in nums[1:]:
            curSum.append(max(num, curSum[-1] + num))

        return max(curSum)

sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))
