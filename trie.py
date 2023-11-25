class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def get_suggestions(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        suggestions = []
        self._dfs(node, prefix, suggestions)
        return suggestions
    
    def _dfs(self, node, prefix, suggestions):
        if node.is_word:
            suggestions.append(prefix)
        
        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, suggestions)

trie1 = Trie()
trie1.insert("sumin")
trie1.insert("apple")
trie1.insert("banana")
trie1.insert("orange")
trie1.insert("app")
trie1.insert("application")


print(trie1.search("sumin"))
print(trie1.search("ss"))
print(trie1.starts_with("a"))
print(trie1.starts_with("j"))
suggestions = trie1.get_suggestions("app")
print(suggestions) 
