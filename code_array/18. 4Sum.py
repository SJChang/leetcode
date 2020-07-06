class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        resultList = []
        nums.sort()
        for i in range(0,len(nums)-3):
            for j in range(i+1,len(nums)-2):
                p = j+1
                q = len(nums)-1
                while p != q:
                    summer = nums[i]+nums[j]+nums[p]+nums[q]
                    if summer == target:
                        listT = [nums[i], nums[j], nums[p], nums[q]]
                        if listT not in resultList:
                            resultList.append(listT)
                        p = p + 1
                    elif summer > target:
                        q = q-1
                    else:
                        p = p+ 1
        return resultList
        