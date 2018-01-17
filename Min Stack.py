class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.S = list()


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min is None:
            self.min = x
        else:
            if x < self.min:
                self.min = x
        S.append(x)


    def pop(self):
        """
        :rtype: void
        """
        S.pop()


    def top(self):
        """
        :rtype: int
        """
        return S[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
