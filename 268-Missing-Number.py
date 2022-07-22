class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) + sum((i - nums[i]) for i in range(len(nums)))
