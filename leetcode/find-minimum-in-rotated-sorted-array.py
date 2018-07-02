class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            print("l:{0}, r:{1}, m:{2}".format(l, r, m))
            if nums[l] <= nums[m] <= nums[r]:
                return nums[l]
            elif nums[m] <= nums[r] <= nums[l]:
                r = m
            elif nums[r] <= nums[l] <= nums[m]:
                l = m + 1
        return nums[l]


if __name__ == "__main__":
    obj = Solution()
    nums = [2, 1]
    o = obj.findMin(nums)
    print(o)