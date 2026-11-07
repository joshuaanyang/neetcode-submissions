class WordDictionary:

    def __init__(self):
        self.store={}
        

    def addWord(self, word: str) -> None:
        store = self.store

        for c in word:
            if c not in store:
                store[c] ={}
            
            store = store[c]
        
        store["#"] =True

    

    def search(self, word: str) -> bool:
        

        def dfs(i, store):

            if i == len(word):
                return "#" in store

            if word[i]==".":
                for key in store:
                    if key != "#" and dfs(i+1,store[key]):
                        return True
                
                return False

            if word[i] not in store:
                return False

            return dfs(i+1, store[word[i]])

        return dfs(0,self.store)

        
