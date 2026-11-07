class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums=set(nums)
        res=0

        for num in nums:
            large=0
            if num-1 not in setnums:
                large+=1
                

                while num+1 in setnums:
                    large+=1
                    num+=1
                res=max(res, large)

        return res
                    
        