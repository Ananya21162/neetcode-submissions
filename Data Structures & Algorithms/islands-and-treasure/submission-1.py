class Solution:
    def isValid(self,i,j,M,N):
        return (0<=i<M) and (0<=j<N)
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
      # BFS
      M, N = len(grid), len(grid[0])
      path = [[0,1],[1,0],[-1,0],[0,-1]]
      for i in range(M):
        for j in range(N):
            if grid[i][j] == 0:
                q = deque([])
                q.append([i,j])
                count = 1
                visited = set()
                visited.add((i,j))
                while q:
                    for _ in range(len(q)):
                        idx = q.popleft()
                        for x,y in path:
                            ni, nj = idx[0]+x, idx[1]+y
                            if self.isValid(ni,nj,M,N) and (ni,nj) not in visited and grid[ni][nj]!= 0 and grid[ni][nj] != -1:
                                visited.add((ni,nj))
                                grid[ni][nj] = min(grid[ni][nj],count)
                                q.append([ni,nj])
                    count += 1


