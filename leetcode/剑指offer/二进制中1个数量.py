# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n >= 0:
            return bin(n).count('1')
        else:
            return 32 - bin(abs(n) - 1).count('1')

    def NumberOf1_wrong(self, n):
        # 下面的方法会陷入死循环
        count = 0
        while n != 0:
            print(n)
            count += 1
            n = n & (n - 1)
        return count


if __name__ == "__main__":
    obj = Solution()
    obj.NumberOf1_wrong(-1)
