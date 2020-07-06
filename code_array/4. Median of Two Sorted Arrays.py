class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        numList = []
        result = -1
        while i < len(nums1) and j < len(nums2):
            if (nums1[i] < nums2[j]):
                numList.append(nums1[i])
                i += 1
            else:
                numList.append(nums2[j])
                j += 1
        if ( i == len(nums1)):
            numList.extend(nums2[j:])
        else:
            numList.extend(nums1[i:])

        if (len(numList)%2==1):
            result = numList[len(numList)/2]
        else:
            result = (numList[len(numList)/2] + numList[len(numList)/2 - 1])/2.0
        return result