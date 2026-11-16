class Solution:
    def generate(self,nums,target,i,ans,sub,subSum):
        if target == subSum:
            ans.append(sub[:])
            return
        if i == len(nums) or subSum > target:
            return
        sub.append(nums[i])
        self.generate(nums,target,i,ans,sub,subSum+nums[i])
        sub.pop()
        self.generate(nums,target,i+1,ans,sub,subSum)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        self.generate(nums,target,0,ans,[],0)
        return ans