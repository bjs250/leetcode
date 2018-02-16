class Solution(object):
    def __init__(self):
        self.target = None
        self.ways = 0

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.target = S
        self.recurse(nums, 0, 0)
        return self.ways

    def recurse(self, nums, index, cumsum):
        if index == len(nums):
            if cumsum == self.target:
                self.ways += 1
        else:
            #print(index, cumsum)
            self.recurse(nums, index+1, cumsum + nums[index])
            self.recurse(nums, index+1, cumsum - nums[index])
