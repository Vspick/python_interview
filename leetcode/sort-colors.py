class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        maps = {0: 0, 1:0, 2:0}
        for num in nums:
            maps[num] += 1

        i = 0
        for k in [0, 1, 2]:
            for _ in range(maps[k]):
                nums[i] = k
                i += 1


# answer
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 原地进行排序
        # zero记录的是元素0的右边界
        # two记录的是元素2的左边界
        # one是遍历移动的指针
        zero = -1
        one = 0
        two = len(nums)
        while one < two:
            if nums[one] == 0:
                # 跟前面的换, 而且要交换的元素要么是0，要么是1，所以one要自增一次
                zero += 1
                nums[zero], nums[one] = nums[one], nums[zero]
                one += 1
            elif nums[one] == 2:
                # 跟后面的换，交换过来的元素可能0，1，2，所以one不能自增
                two -= 1
                nums[two], nums[one] = nums[one], nums[two]
            else:
                # 遇到1则需要自增一次
                one += 1