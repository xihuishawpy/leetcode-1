class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for _ in range(nums.count(val)):
            nums.remove(val)  # remove each val one by one
        return len(nums) # return len of nums
