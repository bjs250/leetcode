# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        L = list()
        self.preOrder(root, L)
        # print(L[1:])
        newroot = TreeNode(L[0])
        for val in L[1:]:
            self.put(TreeNode(val), newroot)

        W = list()
        self.preOrder(newroot, W)
        print(W)

    def preOrder(self, root, L):
        if root:
            L.append(root.val)
            self.preOrder(root.left, L)
            self.preOrder(root.right, L)

    def put(self, node, rel_root):
        if node.val < rel_root.val:
            if rel_root.left:
                self.put(node, rel_root.left)
            else:
                rel_root.left = node
        else:
            if rel_root.right:
                self.put(node, rel_root.right)
            else:
                rel_root.right = node

s = Solution()
L = list()
for i in range(10):
    L.append(TreeNode(i))

L[4].left = L[2]
L[4].right = L[7]
L[2].left = L[1]
L[2].right = L[3]
L[7].left = L[6]
L[7].right = L[9]

s.invertTree(L[4])
