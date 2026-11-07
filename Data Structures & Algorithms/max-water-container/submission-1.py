class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxV=0

        l=0
        r=len(heights)-1

        while l<r:
            if heights[l]<=heights[r]:
                v = heights[l]*(r-l)
                maxV=max(maxV,v)
                l+=1
            elif heights[l]>heights[r]:
                v = heights[r]*(r-l)
                maxV=max(maxV,v)
                r-=1
        
        return maxV

        