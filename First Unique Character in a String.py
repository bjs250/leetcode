class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        odict = {}
        idict = {}
        for index, element in enumerate(s):
            try:
                odict[element] += 1
            except:
                odict[element] = 1
            idict[element] = index
        minimum = float("inf")
        for k in odict.keys():
            if odict[k] == 1:
                if idict[k] < minimum:
                    minimum = idict[k]
        if minimum == float("inf"):
            return -1
        else:
            return minimum
        #print(odict)
        #print(idict)

s = Solution()
print s.firstUniqChar('leetcode')
print s.firstUniqChar('loveleetcode')
