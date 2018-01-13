class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        nmax = 0
        for i in range(0, len(s)):
            n = 0
            if (len(s) - i) < nmax:
                break
            for j in range(i, len(s)):
                if s[j] in d:
                    break  # something was found in the dict
                else:
                    d[s[j]] = 1  # add current to dict
                n += 1
            if (n > nmax):
                nmax = n
            d.clear()
        return nmax

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
