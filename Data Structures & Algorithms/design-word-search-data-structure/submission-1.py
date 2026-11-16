class TrieNode:
    def __init__(self):
        self.links = [None] * 26
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

   

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i],TrieNode())
            node = node.get(word[i])
        node.setEnd()

    def search(self, word: str) -> bool:
        node = self.root

        def dfs(node,word,i):
            if i == len(word):
                return node.getEnd()
            
            if word[i] == ".":
                # search all the 26  values in TrieNode 
                for j in range(26):
                    if node.get(chr(j+ord('a'))):
                        if dfs(node.get(chr(j+ord('a'))),word,i+1):
                            return True
                return False
            else:
                if node.get(word[i]):
                        if dfs(node.get(word[i]),word,i+1):
                            return True
                
                return False

        return dfs(node,word,0)
               
