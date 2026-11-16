class Solution:
    def isValid(self,i,j,M,N):
        return (0<=i<M) and (0<=j<N)

    def dfs(self,i,j,M,N,grid,visited,perm):
        if not self.isValid(i,j,M,N):
            return
        path = [[0,1],[1,0],[-1,0],[0,-1]]
        perm[0] += 4
        for x,y in path:
            ni, nj = i+x,j+y
            if self.isValid(ni,nj,M,N) and grid[ni][nj] == 1:
                perm[0] -= 1
                if not visited[ni][nj]:
                    visited[ni][nj] = True
                    self.dfs(ni,nj,M,N,grid,visited,perm)
        return
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M,N = len(grid), len(grid[0])
        visited = [[False]*N for _ in range(M)]
        perm = [0]
        for i in range(M):
            for j in range(N):
                if not visited[i][j] and grid[i][j]== 1:
                    visited[i][j] = True
                    self.dfs(i,j,M,N,grid,visited,perm)
        return perm[0]
            