class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        store={}

        for i in range(len(numbers)):
            if target-numbers[i] in store:
                return [store[target-numbers[i]], i+1]
            else:
                store[numbers[i]] = i+1

        