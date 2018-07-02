class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in xrange(1, m):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0
        for j in xrange(1, n):
            dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] if obstacleGrid[i][j] == 0 else 0
        return dp[-1][-1]


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[1]
        for i in range(n-1):
            dp.append(0)
        for i in range(0,m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                elif j==0:
                    dp[j]=dp[j]
                else:
                    dp[j]=dp[j]+dp[j-1]
        return dp[-1]