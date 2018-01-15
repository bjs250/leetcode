import time

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # t0 = time.time()
        # Find the start of the unsorted zone
        start_index = 0
        end_index = 0
        same = 0
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                start_index = i-1
                flag = 1
                break
            elif (nums[i] == nums[i-1]):
                same += 1
            else:
                same = 0
        if flag == 1:
            start_index -= same
        # Find the end of the unsorted zone
        same = 0
        for j in range(1, len(nums)):
            if (nums[len(nums)-j-1] > nums[len(nums)-j]):
                end_index = len(nums)-j+1
                break
            elif (nums[len(nums)-j-1] == nums[len(nums)-j]):
                same += 1
            else:
                same = 0
        # t1 = time.time()
        if end_index > 0:
            end_index += same
        result = end_index-start_index
        # print("time elapsed: " + str(t1-t0))
        return result

s = Solution()
# nums = [2, 6, 4, 8, 10, 9, 15] # 5
#  nums = [1,3,2,2,2] # 4
# nums = [1,1] # 0
# nums = [2,3,3,2,4] # 3
print(s.findUnsortedSubarray(nums))
