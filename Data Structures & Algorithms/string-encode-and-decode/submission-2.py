class Solution:

    def encode(self, strs: List[str]) -> str:
        
        ts = ""

        for word in strs:
            
            ts+=str(len(word))+"#"+word
             
        return ts


    def decode(self, s: str) -> List[str]:

        x = []
        i = 0

        while i < len(s):
            j=i

            while s[j] != "#":
            
                j+=1
            l=int(s[i:j])
            myw=s[j+1:j+1+l]
            x.append(myw)
            i=j+1+l

        return x

