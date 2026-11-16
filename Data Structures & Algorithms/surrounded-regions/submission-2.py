class Solution:
    def isValid(self,i,j,M,N):
        return (0<=i<M) and (0<=j<N)
    def dfs(self,visited, board,i,j,M,N,sub):
        visited[i][j] = True
        sub.append([i,j])
        path = [[0,1],[1,0],[-1,0],[0,-1]]
        is_surrounded = True
        for x,y in path:
            ni,nj = i+x,j+y
            if self.isValid(ni,nj,M,N) and board[ni][nj] == "O":
                if not self.isNonB(ni,nj,M,N):
                    is_surrounded = False
                if not visited[ni][nj]:
                    if not self.dfs(visited, board,ni,nj,M,N,sub):
                        is_surrounded = False
        return is_surrounded
    def isNonB(self,i,j,M,N):
        return (0<i<M-1) and (0<j<N-1)
    def solve(self, board: List[List[str]]) -> None:
        M,N = len(board), len(board[0])
        visited = [[False]*N for _ in range(M)]
       
        for i in range(M):
            for j in range(N):
                if self.isNonB(i,j,M,N) and not visited[i][j] and board[i][j] == "O":
                    sub= []
                    if self.dfs(visited, board,i,j,M,N,sub):
                        for x,y in sub:
                             board[x][y] = "X"