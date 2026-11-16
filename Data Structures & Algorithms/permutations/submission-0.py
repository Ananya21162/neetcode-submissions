class Solution:
    def generate(self,nums,pick,ans,sub):
        if len(sub) == len(nums):
            ans.append(sub[:])
            return
        
        for i in range(len(nums)):
            if not pick[i]:
                pick[i] = True
                sub.append(nums[i])
                self.generate(nums,pick,ans,sub)
                sub.pop()
                pick[i] = False
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.generate(nums,[False]*len(nums),ans,[])
        return ans
