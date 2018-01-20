class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
        for index, element in enumerate(alphabet):
            d[element] = index + 1
        total = 0
        for index, element in enumerate(s[::-1]):
            #print(element,index)
            value = 26**index*d[element]
            #print(value)
            total += value
        return total

s = Solution()
print(s.titleToNumber('AB'))
