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
        x = 0
        n = 0
        while l1 is not None:
            x = x + (l1.val) * 10**n
            l1 = l1.next
            n = n + 1
        y = 0
        n = 0
        while l2 is not None:
            x = x + (l2.val) * 10**n
            l2 = l2.next
            n = n + 1
        z = str(x + y)
        z = z[::-1]
        root = ListNode(0)
        prev_node = root
        for c in z:
            current_node = ListNode(int(c))
            prev_node.next = current_node
            prev_node = current_node
        return root.next


s = Solution()
l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)
l4.next = l5
l5.next = l6
root = s.addTwoNumbers(l1, l4)
while root is not None:
    print root.val
    root = root.next
