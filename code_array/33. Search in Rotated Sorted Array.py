class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums: 
            return -1
        
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left+right)/2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[right]: #右邊有序
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1 #在右邊
                else:
                    right = mid -1 #在左邊
            else: #左邊區塊
                if target < nums[mid] and target >= nums[left]:
                    right = mid -1
                else:
                    left = mid + 1
        return -1