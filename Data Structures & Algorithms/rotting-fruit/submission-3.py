class Solution:
    def isValid(self,i,j,M,N):
        return (0<=i<M) and (0<=j<N)
    def orangesRotting(self, grid: List[List[int]]) -> int:    
        M, N = len(grid), len(grid[0])
        q = deque([])
        visited = set()
        fresh_count = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    visited.add((i,j))
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0: return 0
        
        count = 0
        path = [[0,1],[1,0],[-1,0],[0,-1]]
        
        while q:
            if fresh_count == 0: break
            for _ in range(len(q)):
                idx = q.popleft()
                for x,y in path:
                    ni, nj = idx[0]+x, idx[1]+y
                    if self.isValid(ni,nj,M,N) and (ni,nj) not in visited and grid[ni][nj] ==1:
                        visited.add((ni,nj))
                        q.append([ni,nj])
                        grid[ni][nj] = 2
                        fresh_count -= 1
            count += 1
            
        
        return count if fresh_count == 0 else -1