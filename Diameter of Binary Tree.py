#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.max = 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse(root, self.max)

    def traverse(self, root, self.max):
        if not root:
            return 0
        else:
            L = self.traverse(root, root.left, self.max)
            R = self.traverse(root, root.right, self.max)
            return max(L, R)
