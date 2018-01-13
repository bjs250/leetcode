class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        skip = 0
        for i in range(len(s)):
            if skip == 1:
                skip = 0
                continue
            if s[i] == 'M':
                total += 1000
            elif s[i] == 'C':
                if (i != len(s) - 1) and s[i+1] == 'M':
                    total += 900
                    skip = 1
                elif (i != len(s) - 1) and s[i+1] == 'D':
                    total += 400
                    skip = 1
                else:
                    total += 100
            elif s[i] == 'X':
                if (i != len(s) - 1) and s[i+1] == 'C':
                    total += 90
                    skip = 1
                elif (i != len(s) - 1) and s[i+1] == 'L':
                    total += 40
                    skip = 1
                else:
                    total += 10
            elif s[i] == 'I':
                if (i != len(s) - 1) and s[i+1] == 'X':
                    total += 9
                    skip = 1
                elif (i != len(s) - 1) and s[i+1] == 'V':
                    total += 4
                    skip = 1
                else:
                    total += 1
            elif s[i] == 'V':
                total += 5
            elif s[i] == 'L':
                total += 50
            elif s[i] == 'D':
                total += 500
        return total


s = Solution()
print s.romanToInt("MMMCMXCIX")  # 3999
print s.romanToInt("MCDXLIV")  # 1444
print s.romanToInt("DCXXI")  # 621
