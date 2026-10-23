class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            x = "".join(sorted(s))
            y = "".join(sorted(t))

            if x == y:
                return True
            return False

        return False
        