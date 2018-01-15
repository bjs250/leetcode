class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictMap = {}
        for index, value in enumerate(nums):
            print dictMap
            print (target - value)
            if target - value in dictMap:
                return dictMap[target - value], index
            dictMap[value] = index

s = Solution()
print(s.twoSum([8, 11, 10, 12, 7, 5, 24], 13))
#print(s.twoSum([0,4,3,0], 0))
