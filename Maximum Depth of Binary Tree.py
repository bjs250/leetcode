class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        n = 1
        self.nmax = 0
        self.preOrder(root, n)
        return self.nmax

    def preOrder(self, root, n):
        if root:
            if n > self.nmax:
                self.nmax = n
            self.preOrder(root.left, n + 1)
            # print("node:" + str(root.val), "depth:" + str(n), "maxdepth:" + str(self.nmax))
            self.preOrder(root.right, n + 1)


s = Solution()
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
one.left = two
two.left = four
one.right = three
two.right = five
print(s.maxDepth(one))
