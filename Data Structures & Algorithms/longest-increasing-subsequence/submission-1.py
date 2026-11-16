class Solution:
    def maxS(self,i,parent,currL,ans,nums,n):
        if i == -1:
            ans[0] = max(ans[0],currL)
            return
        if parent is not None:
            if nums[parent] > nums[i]:
                self.maxS(i-1,i,currL+1,ans,nums,n)
            self.maxS(i-1,parent,currL,ans,nums,n)
        else:
            self.maxS(i-1,i,currL+1,ans,nums,n)
            self.maxS(i-1,parent,currL,ans,nums,n)

    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [-1]
        n = len(nums)
        self.maxS(n-1,None,0,ans,nums,n)
        return ans[0]