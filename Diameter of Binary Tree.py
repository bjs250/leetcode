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
        self.traverse(root)
        return self.max - 1

    def traverse(self, root):
        if not root:
            return 0
        else:
            L = self.traverse(root.left)
            R = self.traverse(root.right)
            self.max = max(self.max, L+R+1)
            return max(L,R)+1
