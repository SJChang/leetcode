import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # bucket sort solution

        dic = {}
        n = len(nums)

        # O(n) time used
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        # use heap to find out the top K frequent element
        # O(m log k) where m is the number of unique elements
        h = []
        for key in dic:
            heapq.heappush(h, (dic[key], key))
            while len(h) > k:
                heapq.heappop(h)


        return map(lambda tup: tup[1], h)