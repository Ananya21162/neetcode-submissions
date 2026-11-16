class Solution:
    def maxP(self,n,dp):
        if n == 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        product = 0
        for i in range(1, n):
            product = max(product,i*(n-i),i*self.maxP(n-i,dp))
        dp[n] = product
        return dp[n]
    def integerBreak(self, n: int) -> int:
        dp = [-1]*(n+1)
        self.maxP(n,dp)
        return dp[n]