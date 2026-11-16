class Solution:
    def generate(self,nums,pick,res,perm):
        if len(nums) == len(perm):
            res.append(perm[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                if i-1 >= 0 and nums[i] == nums[i-1] and not pick[i-1]:
                    continue
                perm.append(nums[i])
                pick[i] = True
                self.generate(nums,pick,res,perm)
                pick[i] = False
                perm.pop()
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.generate(nums,[False]*len(nums),res,[])
        return res