class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        intermediate = []
        ans=[]
        for num in nums:
            if num not in myDict:
                myDict[num] = 1
            else:
                myDict[num] += 1

        sorted_items = sorted(myDict.items(), key=lambda x: x[1], reverse=True)

        return [num for num, count in sorted_items[:k]]