class Solution:
    def isPalindrome(self, s: str) -> bool:
        mystring = "".join([i.lower() for i in s if i.isalnum()])
        l=0
        r=len(mystring) -1

        for i in range(0,len(mystring)):
            if l < r:
                if mystring[l] != mystring[r]:
                    return False
                else:
                    l+=1
                    r-=1

        # for i,char in enumerate(mystring):
        #     if l < r:
        #         do saomething 

        return True