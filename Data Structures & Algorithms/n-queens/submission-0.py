class Solution:
    def isValid(self,p,q,n):
        return (0<=p<n) and (0<=q<n)

    def isSafe(self,i,j,board,n):
        path = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        for x, y in path:
            ni, nj = i+x, j+y
            while(self.isValid(ni,nj,n)):
                if board[ni][nj] == "Q":
                    return False
                ni += x
                nj += y
        return True
            
    def generate(self,i,n,res,board):
        if i == n: # where i is ith row
            res.append(["".join(row) for row in board])
            return
        for j in range(n):
            if self.isSafe(i,j,board,n):
                board[i][j] = "Q"
                self.generate(i+1,n,res,board)
                board[i][j] = "."
    def solveNQueens(self, n: int) -> List[List[str]]:
       res = []
       board = [["."]*n for _ in range(n)]
       self.generate(0,n,res,board)
       return res