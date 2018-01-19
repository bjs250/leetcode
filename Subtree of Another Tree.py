# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        pass

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.code = ''
        self.traverse(s)
        sstring = self.code
        #print(self.code)
        self.code = ''
        self.traverse(t)
        tstring = self.code
        #print(self.code)
        if tstring in sstring:
            return True
        else:
            return False

    def traverse(self, root):
        if not root:
            self.code = ''.join([self.code, 'N'])
        else:
            self.code = ''.join([self.code, '!' + str(root.val)])
            self.traverse(root.left)
            self.traverse(root.right)


s = Solution()
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
three.left = four
three.right = five
one = TreeNode(1)
four.left = one
two = TreeNode(2)
four.right = two
zero = TreeNode(0)
#two.left = zero
afour = TreeNode(4)
aone = TreeNode(1)
atwo = TreeNode(2)
afour.left = aone
afour.right = atwo
print(s.isSubtree(three, afour))
