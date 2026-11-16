class Solution:
    def generate(self,nums,i,ans,sub):
        if i == len(nums):
            ans.append(sub[:])
            return
        sub.append(nums[i])
        self.generate(nums,i+1,ans,sub)
        sub.pop()
        self.generate(nums,i+1,ans,sub)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.generate(nums,0,ans,[])
        return ans