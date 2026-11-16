class TrieNode():
    def __init__(self):
        self.links = [None]*26
        self.flag = False

    def containsKey(self,ch):
        return self.links[ord(ch)-ord('a')] != None

    def get(self,ch):
        return self.links[ord(ch)-ord('a')]
    
    def put(self,ch,Node):
        self.links[ord(ch)-ord('a')] = Node

    def setEnd(self):
        self.flag = True

    def getEnd(self):
        return self.flag

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i],TrieNode())
            node = node.get(word[i])
        node.setEnd()

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if node.containsKey(word[i]):
                node = node.get(word[i])
            else:
                return False
        return node.getEnd()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if node.containsKey(prefix[i]):
                node = node.get(prefix[i])
            else:
                return False
        return True
        