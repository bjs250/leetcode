# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        currentNode = head.next
        lastNode = head
        lastNode.next = None
        while currentNode:
            temp = currentNode.next
            currentNode.next = lastNode
            lastNode = currentNode
            currentNode = temp
        return lastNode


s = Solution()
L = list()
for i in range(5):
    L.append(ListNode(i))
for i in range(4):
    L[i].next = L[i+1]
root = L[0]
while root:
    print(root.val)
    root = root.next
print("-------------------")
root =s.reverseList(L[0])
while root:
    print(root.val)
    root = root.next
