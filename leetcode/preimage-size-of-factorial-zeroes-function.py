class Solution(object):
    def preimageSizeFZF(self, K):
        """
        如果存在n!的尾数0的个数=K的n,则这种n的数量一定是5
        所以问题转化为了查找是否存在一个数字n使得n!的尾数0的个数=K
        这个n的最大值一定是K*5，因为必存在K个5因子。
        然后用二分查找法，找到一个值x，使得5x！的0的个数为K
        5x!的0的个数 = x + x/5 + x/(5*5) + x/(5*5*5)... 即提供5因子的数量
        :type K: int
        :rtype: int
        """
        l = 0
        r = K
        while l <= r:
            m = (l + r) // 2
            tmp_m = m
            z_num = 0
            while tmp_m > 0:
                z_num += tmp_m
                tmp_m = tmp_m // 5
            if z_num == K:
                return 5
            elif z_num < K:
                l = m + 1
            else:
                r = m - 1
        return 0
