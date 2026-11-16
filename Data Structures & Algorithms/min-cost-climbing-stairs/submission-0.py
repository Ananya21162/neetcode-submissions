class Solution:
    def findCost(self,i,cost,dp):
        if i <0:
            return 0
        if dp[i] != -1:
            return dp[i]
        dp[i] = min(cost[i]+self.findCost(i-1,cost,dp),cost[i]+self.findCost(i-2,cost,dp) )
        
        return dp[i]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]* (n+1)
        left = self.findCost(n-1,cost,dp)
        right = self.findCost(n-2,cost,dp)
        return min(left,right)