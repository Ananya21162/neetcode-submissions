class Solution:
    def countCoin(self,coins,amount,dp):
        if amount == 0: 
            dp[0] = 0
            return 0
       
        if dp[amount] != -1:
            return dp[amount]
        res = float('inf')
        for i in reversed(coins):
            if amount-i >= 0:
                res = min(res,1 + self.countCoin(coins, amount-i,dp))
        dp[amount] = res
        return dp[amount]
       
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [-1] * (amount+1)
        self.countCoin(coins, amount,dp)
        return -1 if dp[amount == float('inf')] else dp[amount]
