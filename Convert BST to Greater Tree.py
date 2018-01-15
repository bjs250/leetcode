# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.inOrder(root)
        return root

    def inOrder(self, root):
        if root:
            self.inOrder(root.right)
            self.total += root.val
            root.val = self.total
            self.inOrder(root.left)


s = Solution()
#five = TreeNode(5)
#two = TreeNode(2)
#five.left = two
#thirteen = TreeNode(13)
#five.right = thirteen
#s.convertBST(five)
two = TreeNode(2)
one = TreeNode(1)
three = TreeNode(3)
two.left = one
two.right = three
newroot = s.convertBST(two)
