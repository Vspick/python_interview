# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            cur1 = l1
            cur2 = l2
            new_lists = None
            cur_new = None
            while cur1 is not None and cur2 is not None:
                if cur1.val < cur2.val:
                    new_node = cur1
                    cur1 = cur1.next
                else:
                    new_node = cur2
                    cur2 = cur2.next

                if new_lists is None:
                    new_lists = new_node
                    cur_new = new_lists
                else:
                    cur_new.next = new_node
                    cur_new = cur_new.next

            if cur1 is not None:
                cur_new.next = cur1
            if cur2 is not None:
                cur_new.next = cur2
            return new_lists


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p=ListNode(0)  # 用一个多余节点解决头节点初始化问题
        h=p
        while l1 and l2:
            if l1.val<=l2.val:
                h.next=l1
                l1=l1.next
            else:
                h.next=l2
                l2=l2.next
            h=h.next
        h.next=l1 or l2
        return p.next



