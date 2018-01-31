class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        L = list()
        while n != 1:
            L.append(n)
            total = 0
            for c in str(n):
                total += int(c)**2
            n = total
            if n in L:
                return False
        return True
        
