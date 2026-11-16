class Solution:
    def generate(self, nums, target,i,ans,sub):
        if target == 0:
            ans.append(sub[:])
            return
        if i == len(nums) or target < 0:
            return
        sub.append(nums[i])
        self.generate(nums,target-nums[i],i+1,ans,sub)
        sub.pop()
        for j in range(i+1,len(nums)):
            if nums[j] != nums[i]:
                self.generate(nums,target,j,ans,sub)
                return
        self.generate(nums,target,len(nums),ans,sub)
                
            
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.generate(candidates,target,0,ans,[])
        return ans