class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedkeys=collections.defaultdict(list)

        for word in strs:
            s="".join(sorted(word))
            
            sortedkeys[s].append(word) 
            
        res=[]

        for key,value in sortedkeys.items():
            res.append(value)

        return res
        