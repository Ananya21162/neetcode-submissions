class Solution:
    def countS(self,n,dp):
        if n == 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        count = float('inf')
        for i in range(int(math.sqrt(n)),0,-1):
            count = min(count,1+ self.countS(n-(i*i),dp))
        dp[n] = count
        return dp[n]
        
    def numSquares(self, n: int) -> int:
        dp = [-1]*(n+1)
        self.countS(n,dp)
        return dp[n]