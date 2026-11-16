class Solution:
    def amount(self,i,dp,nums):
        if i < 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        dp[i] = max(self.amount(i-1,dp,nums) , nums[i]+self.amount(i-2,dp,nums))
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = [-1] * (n)
        dp2 = [-1]* (n)
        left = self.amount(n-2,dp1,nums[1:])
        right = self.amount(n-2,dp2,nums[:-1])
        return max(left,right)