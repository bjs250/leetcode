class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        n = 0
        nmax = 1
        flag = 0
        for i in range(len(s)):
            if s[i] in d.keys():
                flag = 1
                n = i - d[s[i]]
                if n > nmax:
                    nmax = n
            d[s[i]] = i
        if s == "":
            nmax = 0
        if flag == 0:
            return len(d.keys())
        return nmax


s = Solution()
print(s.lengthOfLongestSubstring("au"))
