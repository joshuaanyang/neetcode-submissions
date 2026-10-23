class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = [1]*len(nums)
        
        p=1
        for i in range(len(nums)):
            x[i]=p
            p*= nums[i]

        s=1
        for i in range(len(nums)-1,-1,-1):
            x[i]*=s
            s*=nums[i]


        return x


        