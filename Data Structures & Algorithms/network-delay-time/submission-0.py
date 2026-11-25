class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append((v,t))
        
        minHeap = [ (0,k)]
        heapq.heapify(minHeap)
        visit=set()
        res_time=0

        while minHeap:
            path_time,node=heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res_time=max(res_time,path_time)

            for node_nei, path_time_nei in graph[node]:
                if node_nei not in visit:
                    heapq.heappush(minHeap, (path_time+path_time_nei,node_nei))

        return res_time if len(visit)==n else-1


        