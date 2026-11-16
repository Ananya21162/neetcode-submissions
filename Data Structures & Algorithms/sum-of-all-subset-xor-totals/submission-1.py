
#sub = two choices for every element
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = [0]
        
        def subXOR(nums,subXSum,i,ans):
            if i == len(nums):
                ans[0] += subXSum
                return
            subXOR(nums,subXSum^nums[i],i+1,ans)
            subXOR(nums,subXSum,i+1,ans)

        subXOR(nums,0,0,ans)
        return ans[0]