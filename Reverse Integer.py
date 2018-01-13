class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0] == "-":
            sign = -1
            num = s[1::]
        else:
            sign = 1
            num = s
        result = sign * int(num[::-1])
        if abs(result) > (2**31 - 1):
            return 0
        else:
            return result


s = Solution()
print s.reverse(123)
print s.reverse(-123)
print s.reverse(120)
print s.reverse(1534236469)
print s.reverse(-2147483648)
