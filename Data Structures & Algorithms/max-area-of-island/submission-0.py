class Solution:
    def isValid(self,i,j,M,N):
        return (0<=i<M) and (0<=j<N)
    def dfs(self,grid,visited,i,j,M,N,curr):
        curr[0] += 1
        visited[i][j] = True
        path = [[0,1],[1,0],[-1,0],[0,-1]]
        for x, y in path:
            ni,nj = x+i, y+j
            if self.isValid(ni,nj,M,N) and not visited[ni][nj] and grid[ni][nj] == 1:
                self.dfs(grid,visited,ni,nj,M,N,curr)
     
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        visited = [[False]*N for _ in range(M)]
        count = 0
        curr = [0]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and not visited[i][j]:
                    self.dfs(grid,visited,i,j,M,N,curr)
                    count = max(count,curr[0])
                    curr = [0]
        
        return count
        