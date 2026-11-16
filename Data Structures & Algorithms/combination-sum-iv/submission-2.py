class Solution:
    def countC(self,target,nums,dp):
        if target == 0:
            dp[0] = 1
            return 1
        if target < 0:
            return 0
        if dp[target] != -1:
            return dp[target]
        count = 0
        for i in range(len(nums)):
            count += self.countC(target-nums[i],nums,dp)
        dp[target] = count
        return dp[target]
        
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target+1)
        self.countC(target,nums,dp)
        return dp[target]