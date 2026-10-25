class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        max_list=[]
        l=0
        q=deque()
        

        for r in range(len(nums)):

            while q and nums[q[-1]]< nums[r]:
                q.pop()

            q.append(r)

            if q[0]<l:
                q.popleft()

            if r-l+1 >= k:
                max_list.append(nums[q[0]])
                l+=1
            
        return max_list
                


            
                



        