class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}

        for i,x in enumerate(nums):
            if (target - x) in ans:
                return [ans[target - x],i]
            else:
                ans[x] = i
        