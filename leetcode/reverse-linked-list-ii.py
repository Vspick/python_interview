# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        h = ListNode(-1)
        h.next = head
        first_part_tail = h
        for _ in range(m - 1):
            first_part_tail = first_part_tail.next
        cur = first_part_tail.next
        r_tail = r_head = cur
        cur = cur.next
        for _ in range(m, n):
            cur_tmp = cur
            cur = cur.next
            cur_tmp.next = r_head
            r_head = cur_tmp
        first_part_tail.next = r_head
        r_tail.next = cur
        return h.next


class SolutionAns(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m - 1):
            pre = pre.next
        cur = pre.next
        for i in range(n - m):
            next = cur.next
            next.next, pre.next, cur.next = pre.next, next, next.next
        return dummy.next
