class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        c1={}
        for char in s1:
            c1[char]=c1.get(char,0)+1
        
        c2={}
        l=0

        for r in range(len(s2)):
            #add r to window
            c2[s2[r]] = c2.get(s2[r],0)+1

            if r-l+1>k:
                #shrink
                #1. reduce count
                c2[s2[l]] -=1
                #2 if its 0, delete 
                if c2[s2[l]] == 0:
                    del c2[s2[l]]
                l+=1
            
            if c1==c2:
                return True
        
        return False


        