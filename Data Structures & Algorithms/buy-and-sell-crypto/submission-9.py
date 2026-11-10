class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res=0

        l=0
        r=0

        while r< len(prices):

            if l==r:
                r+=1
                
            elif prices[l]<prices[r]:
                res=max(res,prices[r]-prices[l])
                r+=1
            elif prices[l]>prices[r]:
                
                l+=1
            else:
                l=r

        return res



        
        