class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_sum = nums[0]
        dp = nums[0]
        for num in nums[1:]:
            dp = num + dp if dp > 0 else num
            max_sum = max_sum if max_sum > dp else dp
        return max_sum
