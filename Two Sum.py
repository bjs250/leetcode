import math


class Solution(object):
    def BinarySearch(self, A, value, low, high):
        if (high < low):
            return None
        mid = (low + high)/2
        if (A[mid] > value):
            return self.BinarySearch(A, value, low, mid-1)
        elif (A[mid] < value):
            return self.BinarySearch(A, value, mid+1, high)
        else:
            return mid

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        snums = sorted(nums)
        n = int(math.ceil(len(snums)/2.0))
        for i in range(0, n+1):
            j = self.BinarySearch(snums, target - snums[i], 0, len(snums)-1)
            if (j is not None):
                if (snums[i] == snums[j]):
                    return [nums.index(snums[i]), nums.index(snums[j], nums.index(snums[i])+1)]
                else:
                    return [nums.index(snums[i]), nums.index(snums[j])]

s = Solution()
#print(s.twoSum([8, 11, 10, 12, 7, 5, 24], 13))
print(s.twoSum([0,4,3,0], 0))
