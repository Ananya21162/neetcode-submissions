class Solution:
    def isValid(self,i,j,n):
        return (0<=i<n) and (0<=j<n)

    def isSafe(self,i,j,n,board):
        path = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        for x,y in path:
            ni,nj = i+x, j+y
            while(self.isValid(ni,nj,n)):
                if board[ni][nj] == "Q":
                    return False
                ni += x
                nj += y
        return True
    def generate(self,i,n,board,count):
        if i == n:
            count[0] += 1
            return
        for j in range(n):
            if self.isSafe(i,j,n,board):
                board[i][j] = "Q"
                self.generate(i+1,n,board,count)
                board[i][j] = "."
    def totalNQueens(self, n: int) -> int:
        count = [0]
        board = [["."]*n for _ in range(n)]
        self.generate(0,n,board,count)
        return count[0]