class Solution:
    def isValid(self,i,j,M,N):
        return (0<=i<M) and (0<=j<N)
    def bfs(self,res,q,visited,heights,M,N):
        while q:
            idx = q.popleft()
            r,c = idx[0], idx[1]
            path = [[0,1],[1,0],[-1,0],[0,-1]]
            for x,y in path:
                nr, nc = r+x, c+y
                if self.isValid(nr,nc,M,N) and not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    q.append((nr,nc))
                    visited[nr][nc] = True
                    res.add((nr,nc))
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = deque([])
        atlantic = deque([])
        pac, at = set(), set()
        M,N = len(heights), len(heights[0])
        vis_pac = [[False]*N for _ in range(M)]
        vis_at = [[False]*N for _ in range(M)]
        for j in range(N):
            pacific.append((0,j))
            atlantic.append((M-1,j))
            pac.add((0,j))
            at.add((M-1,j))
            vis_pac[0][j] = True
            vis_at[M-1][j] = True
        for i in range(M):
            pacific.append((i,0))
            atlantic.append((i,N-1))
            pac.add((i,0))
            at.add((i,N-1))
            vis_pac[i][0] = True
            vis_at[i][N-1] = True
        self.bfs(pac,pacific,vis_pac,heights,M,N)
        self.bfs(at,atlantic,vis_at,heights,M,N)
        
        res = []
        for x,y in pac:
            if (x,y) in at:
                res.append([x,y])
        return res

