class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = [1]*len(nums)
        l=0

        while l < len(nums):
            
            for i,num in enumerate(nums):
                if i != l:
                   x[l]=x[l]*num
            
            l+=1

        return x


        