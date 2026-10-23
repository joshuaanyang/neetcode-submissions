class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        ph = {}
        
        for w in strs:
            key ="".join(sorted(w))

            if key not in ph:
                ph[key] = []
                ph[key].append(w)
            else:
                ph[key].append(w)
        
        for x in ph:
            ans.append(ph[x])
        
        return ans
        