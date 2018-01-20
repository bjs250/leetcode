# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        d = dict()
        while head:
            try:
                if d[head]:
                    return True
            except:
                d[head] = head
                head = head.next
        return False
