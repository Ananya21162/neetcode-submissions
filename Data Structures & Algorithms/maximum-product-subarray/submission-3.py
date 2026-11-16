class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1,1
        for num in nums:
            tmp = currMax * num
            currMax = max(num,currMax*num,currMin*num)
            currMin = min(num,tmp, currMin*num)
            res = max(res,currMax)
            # print(res,currMax,currMin)
            if num == 0:
                currMax, currMin = 1,1
        return res