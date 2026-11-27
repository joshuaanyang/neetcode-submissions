class WordDictionary:

    def __init__(self):
        self.store={}
        

    def addWord(self, word: str) -> None:
        store = self.store

        for char in word:
            if char not in store:
                store[char]={}
            store = store[char]
        
        store["#"] = True

        

    def search(self, word: str) -> bool:

        def dfs(i,store):

            if i == len(word):
                return "#" in store 

            char = word[i]
            
            if char == ".":
                for key in store:
                    if key != "#" and dfs(i+1,store[key]):
                        return True
                return False

            if char not in store:
                return False
            
            return dfs(i+1,store[char])

        return dfs(0,self.store)
        
