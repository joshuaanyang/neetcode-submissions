class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l=0
        res=0
        mychar={}
        
        for r in range(len(s)):
            mychar[s[r]]=mychar.get(s[r],0)+1

            if (r-l+1)- max(mychar.values())>k:
                mychar[s[l]]-=1
                l+=1
            
            res=max(res,(r-l+1))
        
        return res





        