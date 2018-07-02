# coding=utf-8

# https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/description/


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        res = None
        l = 0
        r = len(letters) - 1
        while l <= r:
            m = (l + r) / 2
            if letters[m] > target:
                res = letters[m]
                r = m - 1
            else:
                l = m + 1

        if res is None:
            res = letters[0]

        return res
