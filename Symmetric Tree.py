# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.bool = True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        self.traverse(root, root)
        return self.bool

    def traverse(self, node1, node2):
        if node1 and node2:
            self.traverse(node1.left, node2.right)
            print(node1.val, node2.val)
            if node1.val != node2.val:
                self.bool = False
            self.traverse(node1.right, node2.left)
        else:
            self.bool = False
