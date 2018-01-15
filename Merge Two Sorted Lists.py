# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        prevNode = root
        while (l1 is not None) or (l2 is not None):
            if (l1 is not None):
                x = l1.val
            else:
                x = float("inf")
            if (l2 is not None):
                y = l2.val
            else:
                y = float("inf")
            if (x <= y):
                currentNode = ListNode(x)
                l1 = l1.next
            else:
                currentNode = ListNode(y)
                l2 = l2.next
            prevNode.next = currentNode
            prevNode = currentNode
        return root.next


s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(4)
l1.next = l2
l2.next = l3
l4 = ListNode(1)
l5 = ListNode(3)
l6 = ListNode(4)
l4.next = l5
l5.next = l6
root = s.mergeTwoLists(l1, l4)
while root is not None:
    print root.val
    root = root.next
