class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        L = list()
        bag = set(p)
        for i in range(0, len(s) - len(p) + 1):
            end = i + len(p)
            print(bag)
            if bag.intersection(s[i:end]) == bag:
                L.append(i)
        return L

sol = Solution()
#s = 'cbaebabacd'
#p = 'abc'
#s = 'abab'
#p = 'ab'
s = 'baa'
p = 'aa'
print(sol.findAnagrams(s, p))
