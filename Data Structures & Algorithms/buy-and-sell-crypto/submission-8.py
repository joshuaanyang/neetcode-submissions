class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l=0
        r=l+1
        res=0


        while r < len(prices):
            it=0
            
            if prices[l] <= prices[r]:
                it=prices[r]-prices[l]
                r+=1
                res=max(res,it)
            else:

                l=r
                r+=1
            

        return res

        