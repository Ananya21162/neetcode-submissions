class Solution:
    def generate(self,nums,i,ans,sub):
        if i == len(nums):
            ans.append(sub[:])
            return
        sub.append(nums[i])
        self.generate(nums,i+1,ans,sub)
        sub.pop()
        for j in range(i+1, len(nums)):
            if nums[j] != nums[i]:
                self.generate(nums,j,ans,sub)
                return
        self.generate(nums,len(nums),ans,sub)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.generate(nums,0,ans,[])
        return ans