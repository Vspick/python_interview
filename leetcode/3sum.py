# 主要思路，固定首位，用两个游标向中间靠拢查找
# 注意首位和游标的去重

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums = sorted(nums)
        results = list()
        for cur in range(n - 2):
            if nums[cur] > 0:
                break
            if cur > 0 and nums[cur] == nums[cur - 1]:
                continue
            i = cur + 1
            j = n - 1
            while i < j:
                if nums[cur] + nums[i] + nums[j] == 0:
                    results.append([nums[cur], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif nums[cur] + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    i += 1
        return results



class Solution1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        results = list()
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append((nums[i], nums[j], nums[k]))
        results = list(set(results))
        results = map(list, results)
        return results


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        results = list()
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if j >= i + 2 and nums[j] == nums[j - 1]:
                    continue
                t = 0 - nums[i] - nums[j]
                if nums[-1] < t:
                    continue
                l = j + 1
                r = n - 1
                while l <= r:
                    m = (l + r) // 2
                    if nums[m] == t:
                        results.append((nums[i], nums[j], nums[m]))
                        break
                    elif nums[m] < t:
                        l = m + 1
                    else:
                        r = m - 1
        results = list(set(results))
        results = map(list, results)
        return results


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]
        zeros = [num for num in nums if num == 0]
        pos_n = len(positive)
        neg_n = len(negative)
        results = list()

        if len(zeros) >= 3:  # 全是0
            results.append((0, 0, 0))
        if len(positive) >= 2 and len(negative) >= 1:   # 两个正数，一个负数
            for i in range(pos_n - 1):
                for j in range(i + 1, pos_n):
                    t = 0 - positive[i] - positive[j]
                    if negative[0] > t:
                        continue
                    l = 0
                    r = neg_n - 1
                    while l <= r:
                        m = (l + r) // 2
                        if negative[m] == t:
                            results.append((negative[m], positive[i], positive[j]))
                            break
                        elif negative[m] < t:
                            l = m + 1
                        else:
                            r = m - 1
        if len(negative) >= 2 and len(positive) >= 1:  # 两个负数，一个正数
            for i in range(neg_n - 1):
                for j in range(i + 1, neg_n):
                    t = 0 - negative[i] - negative[j]
                    if positive[-1] < t:
                        continue
                    l = 0
                    r = pos_n - 1
                    while l <= r:
                        m = (l + r) // 2
                        if positive[m] == t:
                            results.append((negative[i], negative[j], positive[m]))
                            break
                        elif positive[m] < t:
                            l = m + 1
                        else:
                            r = m - 1
        if len(zeros) >= 1 and len(positive) >= 1 and len(negative) >= 1:  # 一个正数，一个负数，一个0
            for i in range(pos_n):
                t = 0 - positive[i]
                if negative[0] > t:
                    continue
                l = 0
                r = neg_n - 1
                while l <= r:
                    m = (l + r) // 2
                    if negative[m] == t:
                        results.append((negative[m], 0, positive[i]))
                        break
                    elif negative[m] < t:
                        l = m + 1
                    else:
                        r = m - 1

        results = list(set(results))
        results = map(list, results)
        return results