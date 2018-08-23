# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fake_head = ListNode(0)
        tmp_node = fake_head
        for i in range(n):
            tmp_node.next = ListNode(0)
            tmp_node = tmp_node.next
        pre_head = tmp_node
        tmp_node.next = head
        pos1 = fake_head
        pos2 = head
        while pos2 is not None:
            pos1 = pos1.next
            pos2 = pos2.next
        pos1.next = pos1.next.next
        return pre_head.next