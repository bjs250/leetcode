# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = ListNode(0)
        prevNode = root
        while (l1 is not None) or (l2 is not None) or (carry == 1):
            if (l1 is None):
                x = 0
            else:
                x = l1.val
                l1 = l1.next
            if (l2 is None):
                y = 0
            else:
                y = l2.val
                l2 = l2.next
            z = x + y + carry
            carry = 0
            if z >= 10:
                z -= 10
                carry = 1
            l3 = ListNode(z)
            prevNode.next = l3
            prevNode = l3
        return root.next

s = Solution()
l1 = ListNode(5)
l4 = ListNode(5)
l5 = ListNode(9)
l4.next = l5
root = s.addTwoNumbers(l1, l4)
while root is not None:
    print root.val
    root = root.next
