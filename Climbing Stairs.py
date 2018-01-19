class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.m = 0
        self.d = dict()
        self.d[1] = 1
        self.d[2] = 2
        return self.Fib(n)

    def Fib(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            try:
                n2 = self.d[n-2]
            except:
                n2 = self.Fib(n-2)
            try:
                n1 = self.d[n-1]
            except:
                n1 = self.Fib(n-1)
            return self.m + n1 + n2

s = Solution()
print s.climbStairs(35)
