class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        else:
            count = 0
            i = 1
            while i < len(s)+1:
                j = 0
                while j + i < len(s)+1:
                    if s[j:j+i] == s[j:j+i][::-1]:
                        count+=1
                    #print(s[j:j+i], count)
                    j+=1
                i+=1
        return count
