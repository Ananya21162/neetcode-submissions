class Solution:
    def generate(self,candidates, target, sub,ans,i):
        if target == sum(sub):
            ans.append(sub[:])
            return
        if target < sum(sub) or i == len(candidates):
            return
        sub.append(candidates[i])
        self.generate(candidates,target,sub,ans,i+1)
        sub.pop()
        j = i+1
        while j < len(candidates):
            if candidates[j] != candidates[i]:
                break
            j += 1
        self.generate(candidates,target,sub,ans,j)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.generate(candidates,target,[],ans,0)
        return ans

# [1,2,2,4,5,6,9]
