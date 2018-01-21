class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sdict = {}
        tdict = {}
        for c in s:
            try:
                sdict[c] += 1
            except:
                sdict[c] = 1
        for c in t:
            try:
                tdict[c] += 1
            except:
                tdict[c] = 1
        if sdict.keys() == tdict.keys():
            for k in sdict.keys():
                if sdict[k] != tdict[k]:
                    return False
            return True
        else:
            return False

sol = Solution()
s = "rat"
t = "car"
print(sol.isAnagram(s,t))
