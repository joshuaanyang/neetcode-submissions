class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tl = []
        res=[]

        for i in range(len(points)):
            x=points[i][0]
            y=points[i][1]
            z =x**2 + y**2
            tl.append((z,x,y))
        
        tl.sort()

        for i in tl:
            if len(res)< k:
                res.append([i[1],i[2]])
        
        return res
