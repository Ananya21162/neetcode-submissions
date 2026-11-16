class Solution:
    def maxMoney(self,i,dp,nums):
        if i < 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        dp[i] = max(self.maxMoney(i-1,dp,nums), nums[i]+self.maxMoney(i-2 , dp,nums))
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        return self.maxMoney(n-1,dp,nums)
        # return dp[n]