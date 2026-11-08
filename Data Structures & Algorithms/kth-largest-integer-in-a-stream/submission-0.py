class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.store=nums
        self.large_position=k
        

    def add(self, val: int) -> int:
        store=self.store
        store.append(val)
        store.sort()

        for i in range(len(store)-1,-1,-1):
            if len(store)-i == self.large_position:
                return store[i]
        
