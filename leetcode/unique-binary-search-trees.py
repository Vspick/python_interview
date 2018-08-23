class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(root_num, others):
            lefts = [i for i in others if i < root_num]
            rights = [i for i in others if i > root_num]
            left_count = 0
            right_count = 0
            if len(lefts) <= 1:
                left_count = 1
            else:
                for i in range(len(lefts)):
                    r = lefts[i]
                    o = lefts[:i-1] + lefts[i+1:]
                    left_count += helper(r, o)
            if len(rights) <= 1:
                right_count = 1
            else:
                for i in range(len(rights)):
                    r = rights[i]
                    o = rights[:i-1] + rights[i+1:]
                    right_count += helper(r, o)
            return left_count * right_count

        nums = range(1, n + 1)
        count = 0
        for i in range(n):
            r = nums[i]
            o = nums[:i-1] + nums[i+1:]
            count += helper(r, o)
        return count


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        count = 0
        for i in range(1, n + 1):
            left_n = i - 1
            right_n = n - i
            count += self.numTrees(left_n) * self.numTrees(right_n)
        return count


# 正确答案  费了1.5h....
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1]
        for i in range(2, n + 1):
            count = 0
            for j in range(i):
                count += dp[j] * dp[i - j - 1]
            dp.append(count)
        return dp[-1]
