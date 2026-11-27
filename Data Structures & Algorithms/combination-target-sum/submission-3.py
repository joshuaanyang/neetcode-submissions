class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res=[]
        path=[]

        def dfs(i,remainder):
            if remainder==0:
                res.append(path[:])
                return

            if remainder < 0 or i >= len(nums):
                return

            path.append(nums[i])
            dfs(i,remainder-nums[i])
            path.pop()
            dfs(i+1,remainder)
        

        dfs(0,target)
        return res
        