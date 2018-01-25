class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        numrows = list()
        if n == 1:
            numrows.append([1])
            return numrows
        if n == 2:
            numrows.append([1])
            numrows.append([1, 1])
            return numrows
        numrows.append([1])
        numrows.append([1, 1])
        row = list()
        for j in range(2, n):
            row = []
            for i in range(0,j+1):
                if i == 0 or i == j:
                    row.append(1)
                else:
                    row.append(numrows[j-1][i-1]+numrows[j-1][i])
            numrows.append(row)
        return numrows


sol = Solution()
n = 5
print(sol.generate(n))
