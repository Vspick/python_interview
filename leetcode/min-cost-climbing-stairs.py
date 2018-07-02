class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        n = len(cost)
        for i in range(n):
            one, two = cost[n - i - 1] + min(one, two), one
        return min(one, two)

