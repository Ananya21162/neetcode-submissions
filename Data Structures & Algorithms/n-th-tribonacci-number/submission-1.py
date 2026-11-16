class Solution:
    def findN(self,i,dp):
        if i <= 0:
            return 0
        if i <=2:
            return 1
        if dp[i] != -1:
            return dp[i]
        dp[i] = self.findN(i-1,dp) + self.findN(i-2,dp) + self.findN(i-3,dp)
        return dp[i]  
    def tribonacci(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.findN(n,dp)