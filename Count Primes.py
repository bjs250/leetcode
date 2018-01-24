class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        L = n * [1]
        L[0] = 0
        L[1] = 0
        count = 0
        for i in xrange(2,n,1):
            if L[i] == 0:
                continue
            else:
                count += 1
                #print(i)
                for j in xrange(i, n, i):
                    L[j] = 0
        return count

sol = Solution()
n = 8
print(sol.countPrimes(n))
