class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums= set(nums)
        l = 0
        longest = 0

        for num in nums:
            if num -1 not in nums:
                curr = num
                l=1

                while curr +1 in nums:
                    curr += 1
                    l +=1 
                longest = max(l,longest)
        return longest


        

        