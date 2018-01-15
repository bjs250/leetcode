# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        d = {}
        if not root:
            return None
        self.preOrder(root, d)
        #print d
        self.preOrder2(root, d)
        #print d
        self.preOrder3(root, d)
        return root

    def preOrder(self, root, d):
        if root:
            d[root.val] = root.val
            self.preOrder(root.left, d)
            self.preOrder(root.right, d)

    def preOrder2(self, root, d):
        if root:
            #print root.val
            for key in d:
                if root.val > key:
                    d[key] = d[key] + root.val
            self.preOrder2(root.left, d)
            self.preOrder2(root.right, d)

    def preOrder3(self, root, d):
        if root:
            root.val = d[root.val]
            self.preOrder3(root.left, d)
            self.preOrder3(root.right, d)


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
s.convertBST(two)
