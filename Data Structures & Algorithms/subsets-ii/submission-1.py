class Solution:
    def generate(self, nums,sub, res,i):
        if i == len(nums):
            res.append(sub[:])
            return
        sub.append(nums[i])
        self.generate(nums,sub,res,i+1)
        sub.pop()
        j = i+1
        while j < len(nums):
            if nums[j] != nums[i]:
                break
            j += 1
        self.generate(nums,sub,res,j)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.generate(nums,[],res,0)
        return res