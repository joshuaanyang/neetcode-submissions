class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        dicts1 = {}
        for c in s1:
            dicts1[c]=dicts1.get(c,0)+1

        l=0
        window={}

        for r in range(len(s2)):
            window[s2[r]] =  window.get(s2[r],0)+1

            if r-l+1>len(s1):
                window[s2[l]]-=1

                if window[s2[l]] ==0:
                    del window[s2[l]]

                l+=1
            
            if window == dicts1:
                return True

        return False
        