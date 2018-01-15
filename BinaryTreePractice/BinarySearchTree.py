import TreeNode


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        """
        Call the private _put method if there is a root
        If not root, make this the root
        """
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        """
        Recursively add left or right depending on
        1) the value of the key compared to relative root
        2) if we've reached the bottom of the tree
        """
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

        def __setitem__(self, k, v):
            """
            Overload so that BST works like dictionary syntax
            """
            self.put(k, v)

        def get(self, key):
            """
            If there's no root, exit early
            If there is a root, recursively search with private _get method
            """
            if self.root:
                res = self._get(key, self.root)
                if res:
                    return res.payload
                else:
                    return None
            else:
                return None

        def _get(self, key, currentNode):
            """
            if currentNode is nothing, we've hit the bottom and found nothing
            if currentNode is what we've looking for, we're done
            otherwise, recursively look left or right
            """
            if not currentNode:
                return None
            elif currentNode.key == key:
                return currentNode
            elif key < currentNode.key:
                return self._get(key currentNode.leftChild)
            else:
                return self._get(key, currentNode.rightChild)

        def __getitem__(self, key):
            """
            For dictionary syntax to work
            """
            return self.get(key)

        def __contains__(self, key):
            """
            Works with the 'in' syntax now
            """
            if self._get(key, self.root):
                return True
            else:
                return False
