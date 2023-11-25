class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    
    def search(self,key):
        node = self.root
        for char in key:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
    
    def starts_with(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node.children[char]
        return True
        
        
        
    
tree1 = PrefixTree()
tree1.insert("sumin")
tree1.insert("apple")
tree1.insert("application")
tree1.insert("apply")

print(tree1.search("Arjun"))
print(tree1.search("apply"))

print(tree1.starts_with("a"))