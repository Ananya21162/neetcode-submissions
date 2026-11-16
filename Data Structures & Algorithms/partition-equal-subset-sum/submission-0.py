class Solution:
    def check(self,i,S1,S2,nums):
        if i == -1:
            if S1 == S2:
                return True
            return False
        if self.check(i-1,S1+nums[i],S2,nums):
            return True
        if self.check(i-1,S1, S2+nums[i],nums):
            return True
        return False

    def canPartition(self, nums: List[int]) -> bool:
        return self.check(len(nums)-1,0,0,nums)