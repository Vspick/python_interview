class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        nums_len = len(nums)
        most_similar = None
        for i1 in range(0, nums_len - 2):
            i2 = i1 + 1
            i3 = nums_len - 1
            while i2 < i3:
                s = nums[i1] + nums[i2] + nums[i3]
                most_similar = s if most_similar is None or abs(target - most_similar) > abs(target - s) else most_similar
                if s < target:
                    while i2 < i3 and nums[i2] == nums[i2 + 1]:
                        i2 += 1
                    i2 += 1
                elif s > target:
                    while i2 < i3 and nums[i3] == nums[i3 - 1]:
                        i3 -= 1
                    i3 -= 1
                else:
                    return target
        return most_similar


