class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fstack = list()
        bstack = list()
        sindex = None
        bindex = None
        if not nums:
            return []
        else:
            fstack.append(nums[0])
            bstack.append(nums[-1])
        #forward
        for i in range(1, len(nums)):
            if nums[i] >= fstack[-1]:
                fstack.append(nums[i])
            else:
                sindex = i
                # print(sindex)
                while len(fstack) > 0 and nums[i] < fstack[-1]:
                    sindex -= 1
                    fstack.pop()
                break
        #backward
        for i in range(1, len(nums)):
            if nums[len(nums)-1-i] <= bstack[-1]:
                bstack.append(nums[len(nums)-1-i])
            else:
                bindex = len(nums)-1-i
                # print(bindex)
                while len(bstack) > 0 and nums[len(nums)-1-i] > bstack[-1]:
                    bindex += 1
                    bstack.pop()
                break
        if sindex != None and bindex != None:
            print(sindex)
            print(bindex)
            return abs(bindex - sindex) + 1
        else:
            return 0



s = Solution()
# nums = [2, 6, 4, 8, 10, 9, 15] # 5
nums = [2, 1]
print(s.findUnsortedSubarray(nums))
