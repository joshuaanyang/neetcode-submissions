class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myhash = set()
        for num in nums:
            if num not in myhash:
                myhash.add(num)
            else:
                return True
        return False

                
        