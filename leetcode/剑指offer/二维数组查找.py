# -*- coding:utf-8 -*-
class Solution:
    def Find3(self, target, array):
        left = 0
        down = len(array) - 1
        while left < len(array[0]) and down >= 0:
            if array[down][left] == target:
                return True
            elif array[down][left] < target:
                left += 1
            else:
                down -= 1
        return False

    # 暴力法
    def Find2(self, target, array):
        big_array = []
        for sub_array in array:
            big_array += sub_array
        return target in big_array

    # array 二维列表  想复杂了的四边二分查找法
    def Find(self, target, array):
        # write code here
        left = 0
        right = len(array[0]) - 1
        up = 0
        down = len(array) - 1
        while left <= right and up <= down:
            print(left, right, up, down)
            # find up
            u, d = up, down
            while u <= d:
                m = (u + d) // 2
                if array[m][right] == target:
                    return True
                elif array[m][right] < target:
                    u = m + 1
                else:
                    d = m - 1
            up = u
            # find down
            u, d = up, down
            while u <= d:
                m = (u + d) // 2
                if array[m][left] == target:
                    return True
                elif array[m][left] < target:
                    u = m + 1
                else:
                    d = m - 1
            down = d
            # find left
            l, r = left, right
            while l <= r:
                m = (l + r) // 2
                if array[down][m] == target:
                    return True
                elif array[down][m] < target:
                    l = m + 1
                else:
                    r = m - 1
            left = l
            # find right
            l, r = left, right
            while l <= r:
                m = (l + r) // 2
                if array[up][m] == target:
                    return True
                elif array[up][m] < target:
                    l = m + 1
                else:
                    r = m - 1
            right = l


if __name__ == "__main__":
    a = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    target = 42
    obj = Solution()
    r = obj.Find3(target, a)
    print(r)