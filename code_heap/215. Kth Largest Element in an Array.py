import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # heap
        h = nums[:k]
        heapq.heapify(h)
        n = len(nums)
        for i in range(k, n):
            heapq.heappushpop(h, nums[i])

        return heapq.heappop(h)