class Solution:
    def trap(self, height: List[int]) -> int:
        container=0
        l=0
        r= len(height)-1
        leftmax=0
        rightmax=0

        while l<r:
            if height[l]<=height[r]:
                leftmax = max(leftmax,height[l])
                container += leftmax - height[l]
                l+=1
            else:
                rightmax = max(rightmax,height[r])
                container += rightmax - height[r]
                r-=1
            
        return container
        