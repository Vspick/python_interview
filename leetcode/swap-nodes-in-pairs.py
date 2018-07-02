# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_tail = new_head
        cur = head
        while cur and cur.next:
            first = cur
            second = first.next
            cur = second.next
            second.next = first
            new_tail.next = second
            new_tail = first
        new_tail.next = cur
        return new_head.next
