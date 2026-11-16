class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start = 0
        max_len = len(nums)
        res =[]
        res.append(1)
        for i in range(1,len(nums)):
            res.append(math.prod(nums[start:i]))
        res = res[::-1]
        for i in range(1, len(nums)):
            res [i] = res[i] *math.prod(nums[::-1][start:i])
        return res[::-1]

        
                