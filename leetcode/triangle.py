# 注意list直接赋值时是引用，原始数据会一起变化
# 自下向上，解决边界判定

class Solution2(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [0 for _ in range(len(triangle[-1]))]
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            tmp_dp = [x for x in dp]
            print(i, tmp_dp)
            for j in range(i + 1):
                if j == 0:
                    dp[j] = tmp_dp[j] + triangle[i][j]
                elif j == i:
                    dp[j] = tmp_dp[j - 1] + triangle[i][j]
                else:
                    dp[j] = triangle[i][j] + min(tmp_dp[j], tmp_dp[j - 1])
                print(j, dp)
        return min(dp)


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        sums = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                sums[j] = min(sums[j], sums[j + 1]) + triangle[i][j]
        print(triangle)
        return sums[0]


if __name__ == "__main__":
    obj = Solution()
    t = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
        ]
    out = obj.minimumTotal(t)
    print(out)
