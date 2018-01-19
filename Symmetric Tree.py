# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.code = ''
        self.traverseL(root.left)
        L = self.code
        print(L)
        self.code = ''
        self.traverseR(root.right)
        R = self.code
        print(R)
        if L == R:
            return True
        else:
            return False

    def traverseL(self, root):
        if not root:
            self.code += str('N')
        else:
            self.code += '!' + str(root.val)
            self.traverseL(root.left)
            self.traverseL(root.right)

    def traverseR(self, root):
        if not root:
            self.code += str('N')
        else:
            self.code += '!' + str(root.val)
            self.traverseR(root.right)
            self.traverseR(root.left)
