class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        L = list()
        p = primes()
        for i in range(2, n+1):
            L.append(i)
            L[-1] = 0
        print(L)
        while step <
            step = 2
            m = 0
            while m*step < n - 1:
                L[m*step] = 1
                m = m + 1
        print(L)

sol = Solution()
n = 10
print(sol.countPrimes(n))
