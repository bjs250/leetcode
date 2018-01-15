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
        if not root:
            return []

        newroot = TreeNode(root.val)
        self.preOrder(root, newroot, 0)
        return newroot

    def preOrder(self, root, newroot, direction):
        if root:
            if (direction == -1):
                #print(direction, newroot.val)
                newroot.right = TreeNode(root.val)
                newroot = newroot.right
            elif (direction == 1):
                #print(direction, newroot.val)
                newroot.left = TreeNode(root.val)
                newroot = newroot.left
            print(root.val)
            self.preOrder(root.left, newroot, -1)
            self.preOrder(root.right, newroot, 1)


s = Solution()
L = list()
for i in range(10):
    L.append(TreeNode(i))

#root = L[1]
#root.left = L[2]

L[4].left = L[2]
L[4].right = L[7]
L[2].left = L[1]
L[2].right = L[3]
L[7].left = L[6]
L[7].right = L[9]

newroot = s.invertTree(L[4])
print("------------")
print(newroot.val)
#print(newroot.left.val)
#print(newroot.right.val)
