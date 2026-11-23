class PrefixTree:

    def __init__(self):
        self.store={}
        

    def insert(self, word: str) -> None:
        store = self.store

        for char in word:
            if char not in store:
                store[char]={}
            store=store[char]
        
        store["#"] = True


    def search(self, word: str) -> bool:
        store = self.store

        for char in word:
            if char not in store:
                return False
            store=store[char]

        return "#" in store
        

    def startsWith(self, prefix: str) -> bool:
        store = self.store

        for char in prefix:
            if char not in store:
                return False
            store=store[char]
        
        return True
        
        