class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 5:
            return n
        ugly_nums = [1, 2, 3, 4, 5]
        loc = (0, 0, 0)
        for _ in range(n - 5):
            ugly_num, loc = self.get_next_ugly_num(ugly_nums, loc)
            print(ugly_num)
            ugly_nums.append(ugly_num)
        return ugly_nums[-1]

    def get_next_ugly_num(self, ugly_nums, loc):
        s2, s3, s5 = loc
        n = len(ugly_nums)
        max_ugly_num = ugly_nums[-1]
        tmp2 = max_ugly_num // 2
        tmp3 = max_ugly_num // 3
        tmp5 = max_ugly_num // 5
        print(s2, s3, s5, tmp2, tmp3, tmp5)
        pre_ugly_num2 = max_ugly_num
        pre_ugly_num3 = max_ugly_num
        pre_ugly_num5 = max_ugly_num
        for i in range(s2 + 1, n):
            if ugly_nums[i] > tmp2:
                pre_ugly_num2 = ugly_nums[i]
                tmp_s2 = i
                break
        for i in range(s3 + 1, n):
            if ugly_nums[i] > tmp3:
                pre_ugly_num3 = ugly_nums[i]
                tmp_s3 = i
                break
        for i in range(s5 + 1, n):
            if ugly_nums[i] > tmp5:
                pre_ugly_num5 = ugly_nums[i]
                tmp_s5 = i
                break
        next_ugly_num = min(pre_ugly_num2 * 2, pre_ugly_num3 * 3, pre_ugly_num5 * 5)
        if pre_ugly_num2 * 2 == next_ugly_num:
            s2 = tmp_s2
        if pre_ugly_num3 * 3 == next_ugly_num:
            s3 = tmp_s3
        if pre_ugly_num5 * 5 == next_ugly_num:
            s5 = tmp_s5
        return next_ugly_num, (s2, s3, s5)


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2, i3, i5 = 0, 0, 0
        ans = [1]
        while len(ans) < n:
            m2, m3, m5 = ans[i2] * 2, ans[i3] * 3, ans[i5] * 5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            ans.append(m)
        return ans[-1]


class Solution(object):
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ugly[n-1]

if __name__ == "__main__":
    obj = Solution()
    obj.nthUglyNumber(10)
