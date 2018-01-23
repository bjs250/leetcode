class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)
        counter = 0
        print(s)
        for c in s:
            print(c)
            if c == str(1):
                counter = counter + 1
        return counter
