class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path=[]
        res=[]

        def dfs(i,remainder):
            if remainder == 0:
                res.append(path[:])
                return
            
            if i>=len(nums) or remainder <0:
                return
            
            path.append(nums[i])
            dfs(i,remainder-nums[i])
            path.pop()
            
            dfs(i+1,remainder)
        
        dfs(0,target)
        return res

        