class Solution:
    def isValid(self,i,j,M,N):
        return (0<=i<M) and (0<=j<N)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        visited = [[False]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    q = deque([(i,j)])
                    break
        path = [[0,1],[1,0],[-1,0],[0,-1]]
        perm = 0
        while q:
            print(q,perm)
            node = q.popleft()
            i, j = node[0], node[1]
            visited[i][j] = True
            perm += 4
            
            for x,y in path:
                ni, nj = x+i, y+j
                # if not self.isValid()
                if self.isValid(ni,nj,M,N) and grid[ni][nj] == 1:
                    perm -= 1
                    if not visited[ni][nj]:
                        visited[ni][nj] = True
                        q.append((ni,nj))
        return perm
            