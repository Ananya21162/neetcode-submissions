class TrieNode:
    def __init__(self):
        self.links = [None]*26
        self.flag = False
    
    def containsKey(self,ch):
        return self.links[ord(ch)-ord('a')] != None

    def get(self,ch):
        return self.links[ord(ch)-ord('a')]
    
    def put(self,ch,Node):
        self.links[ord(ch)-ord('a')] = Node

    def setEnd(self,value):
        self.flag = value

    def getEnd(self):
        return self.flag

# class Trie:
    
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i],TrieNode())
            node = node.get(word[i])
        node.setEnd(True)

    def isSafe(self,i,j,M,N):
        return (0<=i<M) and (0<=j<N)


    def dfs(self,i,j,board, visited, ans,M,N,node,sub):
        path = [[0,1],[1,0],[-1,0],[0,-1]]
        if node.getEnd():
            ans.append("".join(sub[:]))
            node.setEnd(False)
            # return
        for x,y in path:
            ni,nj = i+x, j+y
            if self.isSafe(ni,nj,M,N) and not visited[ni][nj] and node.containsKey(board[ni][nj]):
                visited[ni][nj] = True
                sub.append(board[ni][nj])
                # print(sub)
                self.dfs(ni,nj,board,visited,ans,M,N,node.get(board[ni][nj]),sub)
                visited[ni][nj] = False
                sub.pop()


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.insert(word)
        
        M,N = len(board), len(board[0])
        visited = [[False]*N for _ in range(M)]
        
        ans = []
        for i in range(M):
            for j in range(N):
                node = self.root
                sub= []
                if node.containsKey(board[i][j]):
                    visited[i][j] = True
                    sub.append(board[i][j])
                    self.dfs(i,j,board, visited, ans,M,N,node.get(board[i][j]),sub)
                    visited[i][j] = False
                    sub.pop()
        return ans




