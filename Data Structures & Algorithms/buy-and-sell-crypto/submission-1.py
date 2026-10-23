class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        l= 0
        r = 1

        while r < len(prices):
            lar=0
            if prices[l]<=prices[r]:
                lar = prices[r]-prices[l]
                result = max(result, lar)
                r+=1
            else:
                l=r
                r+=1
        return result


        