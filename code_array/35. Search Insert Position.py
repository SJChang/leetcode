class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        while i < len(nums):
            if nums[i] < target:
                i += 1
            else:
                break
        return i