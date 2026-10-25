class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        cs={}
        ct={}

        for char in t:
            ct[char] = ct.get(char,0)+1

        have=0
        need=len(ct)

        shortest = float("inf")
        result = [-1,-1]

        for r in range(len(s)):
            char =s[r]
            cs[char] = cs.get(char,0)+1

            if char in ct and cs[char]==ct[char]:
                have+=1

            while have == need:
                if r-l+1 < shortest:
                    shortest = r-l+1
                    result=[l,r]

                #reduce left char
                cs[s[l]]-=1

                #check l on ct
                if s[l] in ct and cs[s[l]] < ct[s[l]]:
                    have-=1
                
                #move left pointer

                l+=1

        if shortest != float("inf"):
            return s[result[0]:result[1]+1]
        else:
            return ""


        

        