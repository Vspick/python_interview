# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):  # 我自己写得蓄水池抽样，有时通过有时报错
        """
        Returns a random node's value.
        :rtype: int
        """
        cur = self.head
        i = 0
        choice = None
        while cur is not None:
            i += 1
            rand_n = random.randint(1, i)
            if rand_n == i:
                choice = cur
            cur = cur.next
        return choice.val

    def getRandom(self):  # 答案
        """
        Returns a random node's value.
        :rtype: int
        """
        result, node, index = self.head, self.head.next, 1
        while node:
            if random.randint(0, index) == 0:
                result = node
            node = node.next
            index = index + 1
        return result.val

    def getRandom1(self):  # 复杂的暴力解法
        """
        Returns a random node's value.
        :rtype: int
        """
        if self.head is None:
            return None
        cur = self.head
        i = 0
        while cur is not None:
            i += 1
            cur = cur.next
        x = random.randint(1, i)
        cur = self.head
        for i in range(x):
            cur = cur.next
        return cur.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()