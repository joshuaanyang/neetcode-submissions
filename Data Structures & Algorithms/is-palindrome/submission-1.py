class Solution:
    def isPalindrome(self, s: str) -> bool:
        mystring = "".join([i.lower() for i in s if i.isalnum()])
        l=0
        r=len(mystring) -1

        while l < r:
            if mystring[l] != mystring[r]:
                return False
            else:
                l+=1
                r-=1

        return True