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
        print snums
        n = int(math.ceil(len(snums)/2.0))
        print "n:" + str(n)
        for i in range(0, n+1):
            print "i:" + str(i)
            print snums[i]
            print(target-snums[i])
            print ("-------")
            j = self.BinarySearch(snums, target - snums[i], 0, len(snums)-1)
            if (j is not None):
                print("hit!")
                print(snums[i])
                print(snums[j])
                print(nums)
                return []




s = Solution()
#nums = [8, 11, 10, 12, 7, 5, 24]
#snums = sorted(nums)
#print snums
#print(s.BinarySearch(snums, 8, 0, len(nums)-1))
print(s.twoSum([8, 11, 10, 12, 7, 5, 24], 13))
