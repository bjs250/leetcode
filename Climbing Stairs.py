class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        L = [1, 1]
        for i in range(2, n+1):
            L.append(L[-1] + L[-2])
        return L[n]


s = Solution()
print s.climbStairs(35)
