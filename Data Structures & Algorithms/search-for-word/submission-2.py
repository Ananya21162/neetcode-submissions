class Solution:
    def isValid(self,i,j,M,N):
        return (0<=i<M) and (0<=j<N)

    def dfs(self,board,visited,word,i,j,M,N,count):
        if count == len(word)-1:
            return True
        visited[i][j] = True
        paths = [[0,1],[1,0],[0,-1],[-1,0]]
        for path in paths:
            ni, nj = i+path[0], j+path[1]
            if self.isValid(ni,nj,M,N) and not visited[ni][nj] and word[count+1] == board[ni][nj]:
                if self.dfs(board,visited,word,ni,nj,M,N,count+1):
                    return True
        visited[i][j] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        M,N = len(board), len(board[0])
        

        for i in range(M):
            for j in range(N):
                visited = [[False]*N for _ in range(M)]
                if word[0] == board[i][j]:
                    if self.dfs(board,visited,word,i,j,M,N,0):
                        return True
    
        return False