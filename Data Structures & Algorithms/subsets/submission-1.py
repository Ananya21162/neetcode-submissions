class Solution:
    def generate(self,nums,ans,i,sub):
        if i == len(nums):
            ans.append(sub[:])
            return
        sub.append(nums[i])
        self.generate(nums,ans,i+1, sub)
        # j = i +1
        # while j < len(nums):
        #     if nums[j] != nums[i]:
        #         break
        #     j += 1
        sub.pop()
        self.generate(nums,ans,i+1,sub)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.generate(nums,ans,0,[])
        return ans

# i =0 ans =[] sub=[1] nums= [1,2,3]
# i = 1 ans =[] sub=[1,2] nums= [1,2,3]
# i = 2 ans =[[1,2,3],[1,2],] sub=[1,2] nums= [1,2,3]
# i =0 ans =[] sub=[1] nums= [1,2,3]