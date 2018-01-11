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
        oldNode = root
        while (l1 is not None or l2 is not None) or carry == 1:
            #print ("l1:" + str(l1.val))
            newNode = ListNode(0)
            oldNode.next = newNode
            if l1 is not None:
                x = l1.val
                l1 = l1.next
            else:
                x = 0
            if l2 is not None:
                y = l2.val
                l2 = l2.next
            else:
                y = 0
            z = x + y
            if z >= 10:
                z = z - 10
                flag = 1
            else:
                flag = 0
            newNode.val = z + carry
            if flag == 1:
                carry = 1
            else:
                carry = 0
            oldNode = oldNode.next
        #print(root.val)
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
print(s.addTwoNumbers(l1, l4))
