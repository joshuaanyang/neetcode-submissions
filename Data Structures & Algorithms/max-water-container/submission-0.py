class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result=0
        l=0
        r=len(heights)-1

        while l < r:
            area = 0
            if heights[l] < heights[r] or heights[l] == heights[r]:
                area = heights[l] * (r-l)
                result = max(result,area)
                l+=1
            elif heights[l] > heights[r] or heights[l] == heights[r]:
                area = heights[r] * (r-l)
                result = max(result,area)
                r-=1
                
        return result

        