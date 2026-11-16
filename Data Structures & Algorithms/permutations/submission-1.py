class Solution:
    def generate(self,nums,perm,res,pick):
        if len(nums) == len(perm):
            res.append(perm[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.generate(nums,perm,res,pick)
                perm.pop()
                pick[i] = False
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.generate(nums,[],res,[False]*len(nums))
        return res