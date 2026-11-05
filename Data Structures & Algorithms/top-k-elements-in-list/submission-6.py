class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        intl=[]
        res=[]

        for num in nums:
            counter[num]=counter.get(num,0)+1

        
        for key, val in counter.items():
            intl.append([val,key])

        intl.sort()

        for i in range(k):
            res.append(intl.pop()[1])
        
        return res


        