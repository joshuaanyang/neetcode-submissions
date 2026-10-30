class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myCount={}
        myorder=[]
        


        for num in nums:
            myCount[num]= myCount.get(num,0)+1

        for key,val in myCount.items():
            myorder.append([val,key])
        
        myorder.sort()
        

        res=[]

        while len(res)<k:
            res.append(myorder.pop()[1])
            
        
        return res





        
            
        