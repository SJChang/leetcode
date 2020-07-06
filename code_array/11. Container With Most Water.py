class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if height == []:
            return 0
        
        l = len(height)
        p1= 0
        p2 = l-1
        ans = 0
        
        while p1<p2:
            ans = max(ans, (min(height[p1],height[p2])*(p2-p1)))
            
            if height[p1] < height[p2]:
                p1 +=1
            else:
                p2 -=1
            
        
        return ans