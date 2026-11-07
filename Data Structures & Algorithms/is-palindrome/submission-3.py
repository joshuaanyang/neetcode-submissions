class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for char in s.lower():
            if char.isalnum():
                new_s+=char

        n = len(new_s)
        r= n-1

        for c in new_s:
            if c != new_s[r]:
                return False
            r-=1
        
        return True
