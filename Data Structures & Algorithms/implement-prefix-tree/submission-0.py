class PrefixTree:

    def __init__(self):
        self.store = {}
        

    def insert(self, word: str) -> None:
        curr=self.store

        for c in word:
            if c not in curr:
                curr[c]={}
            
            curr = curr[c]
        
        curr["#"]=True


    def search(self, word: str) -> bool:
        store=self.store
        for c in word:
            if c not in store:
                return False
            store=store[c]
        
        return "#" in store
        

    def startsWith(self, prefix: str) -> bool:

        store=self.store

        for c in prefix:
            if c not in store:
                return False
            store=store[c]

        return True
        
        