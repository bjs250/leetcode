from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        c = Counter(nums) #O(n)
        output = list()
        for t in c.most_common()[0:k]:
            output.append(t[0])
        return output
