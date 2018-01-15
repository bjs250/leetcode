class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        sp = 0
        n = 0
        for i in range(len(s)):
            if s[i] in d:
                sp = d[s[i]] + 1
            d[s[i]] = i
            if (i - sp + 1) > n:
                n = i - sp + 1
            print s[i], sp, n
        return n


s = Solution()
print(s.lengthOfLongestSubstring("abba"))
#print(s.lengthOfLongestSubstring("aa"))
#print(s.lengthOfLongestSubstring("aab"))
#print(s.lengthOfLongestSubstring(""))
#print(s.lengthOfLongestSubstring("abcabcbb"))
