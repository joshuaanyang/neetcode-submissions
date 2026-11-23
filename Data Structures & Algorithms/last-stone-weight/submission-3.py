class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-x for x in stones]
        heapq.heapify(self.maxHeap)

        while len(self.maxHeap) >1:
            x = -(heapq.heappop(self.maxHeap))
            y = -(heapq.heappop(self.maxHeap))

            if x!=y:
                heapq.heappush(self.maxHeap,-(x-y))
        
        if len(self.maxHeap) ==1:
            return -(heapq.heappop(self.maxHeap))
        
        return 0
            

        
        