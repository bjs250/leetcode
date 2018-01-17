# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.flag = 0
        self.bool = False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        #self.trav(s)
        self.traverse(s, t)
        return self.bool

    def traverse(self, root, sub_root):
        if root:
            if sub_root and (root.val == sub_root.val):
                #print(root.val, sub_root.val)
                self.traverse(root.left, sub_root.left)
                self.traverse(root.right, sub_root.right)
                #print(root.right and root.left)
                if (root.right and root.left):
                    self.bool = True
                else:
                    self.bool = False
            else:
                #print(root.val)
                self.traverse(root.left, sub_root)
                self.traverse(root.right, sub_root)


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
