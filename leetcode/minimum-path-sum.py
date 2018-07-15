class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        for i, c in enumerate(grid[0]):
            dp[i] = c + dp[i - 1] if i > 0 else c

        for i in range(1, m):
            for j in range(n):
                if j > 0:
                    dp[j] = grid[i][j] + min(dp[j - 1], dp[j])
                else:
                    dp[j] = grid[i][j] + dp[j]
        return dp[-1]


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [0] * len(grid)
        # 任选一条路径，初始化距离
        dp[0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i] = dp[i - 1] + grid[i][0]
        for j in range(1, len(grid[0])):
            for i in range(len(grid)):
                dp[i] = min(dp[i], dp[i - 1]) + grid[i][j] if i > 0 else dp[i] + grid[i][j]
        return dp[len(grid) - 1]


if __name__ == "__main__":
    obj = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(obj.minPathSum(grid))
