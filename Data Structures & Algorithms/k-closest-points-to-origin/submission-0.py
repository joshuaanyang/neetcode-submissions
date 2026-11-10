class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap=[]
        mydict={}
        res=[]

        for point in points:
            x=point[0]
            y=point[1]
            c=x**2 + y**2
            minHeap.append((c,x,y))
        
        heapq.heapify(minHeap)
        

        for i in range(k):
            a,b,c = heapq.heappop(minHeap)
            res.append([b,c])
        
        return res
            
        