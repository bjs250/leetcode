from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        L = list()
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        print(c1,c2)
        for k in c1.keys():
            for j in c2.keys():
                if k == j:
                    for m in range(min(c1[k],c2[j])):
                        L.append(k)
        return L
 
