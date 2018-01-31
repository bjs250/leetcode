class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            print(bin(n), bin(n-1), n) 
            n = n&(n-1)
            count += 1
        return count

sol = Solution()
n = 100
sol.hammingWeight(n)
