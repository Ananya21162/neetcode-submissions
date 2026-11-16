class Solution:
    def generate(self,nums,i,ans,subXor):
        if i == len(nums):
            ans[0] += subXor
            return
        
        subXor ^= nums[i]
        self.generate(nums,i+1,ans,subXor)
        subXor ^= nums[i]
        self.generate(nums,i+1,ans,subXor)

    def subsetXORSum(self, nums: List[int]) -> int:
        ans = [0]
        self.generate(nums,0,ans,0)
        return ans[0]