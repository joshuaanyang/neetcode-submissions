class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countfreq = {}
        res = 0

        l=0
        for r in range(len(s)):
            countfreq[s[r]] = countfreq.get(s[r],0) +1

            if (r-l+1) - max(countfreq.values()) > k:
                countfreq[s[l]]-=1
                l+=1
            
            res=max(res,(r-l+1))

        return res

        