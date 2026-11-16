class Solution:
    def isValid(self,i,j,M,N):
        return (0 <= i < M) and (0 <= j < N)
    def dfs(self,i,j,M,N,idx,visited,board,word,ans):
        
        if idx == len(word)-1:
            ans[0] = True
        path = [[0,1],[1,0],[-1,0],[0,-1]]
        for x,y in path:
            ni = i + x
            nj = j + y
            if self.isValid(ni,nj,M,N) and not visited[ni][nj] and idx+1 < len(word) and board[ni][nj] == word[idx+1]:
                visited[ni][nj] = True
                self.dfs(ni,nj,M,N,idx+1,visited,board,word,ans)
                visited[ni][nj] = False
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        visited = [[False]*N for _ in range(M)]
        ans = [False]
        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    self.dfs(i,j,M,N,0,visited,board,word,ans)
                    visited[i][j] = False
                if ans[0]:
                    return True
        return False

