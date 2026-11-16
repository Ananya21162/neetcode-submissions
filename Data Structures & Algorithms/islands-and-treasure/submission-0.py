class Solution:
    def isValid(self,i,j,M,N):
        return (0<=i<M) and (0<=j<N)
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # save all treasure points in queue
        # while q is not empty try reaching all neighbors in grid
        # if curr value is higher than possible, replace & add in queue else continue
        q = deque([])
        M = len(grid)
        N = len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    q.append([i,j])
        path = [[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            node = q.popleft()
            i, j = node[0], node[1]
            for x,y in path:
                ni,nj = x+i, y+j
                if self.isValid(ni,nj,M,N) and grid[ni][nj] != -1:
                    if grid[ni][nj] > grid[i][j]+1:
                        grid[ni][nj] = grid[i][j]+1
                        q.append([ni,nj])
        

