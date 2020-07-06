class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.leftFind(nums, target)
        right = self.rightFind(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]
    
    def leftFind(self, nums, target):
        left, right = 0, len(nums)
        
        while left < right:
            mid = left+(right-left)/2
            if nums[mid] < target:
                left = mid +1
            else:
                right = mid
        return left
        
    
    def rightFind(self, nums, target):
        left, right = 0, len(nums)
        
        while left < right:
            mid = left + (right-left)/2
            if nums[mid] <= target:
                left = mid +1
            else:
                right = mid
        return left