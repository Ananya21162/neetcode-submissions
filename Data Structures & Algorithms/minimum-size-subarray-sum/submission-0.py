class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # keep track of currSub array sum [l,r], if sum >= target update minL : r-l+1
        # is subSum is greater, keep moving l and reduce Sum and update minL
        # if subSum is lesser, increase r
        subSum = 0
        minL = float('inf')
        l, r = 0, 0
        while r < len(nums):
            subSum += nums[r]
            while subSum >= target and l <= r:
                minL = min(minL, r-l+1)
                subSum -= nums[l]
                l += 1
            
            r += 1
        return minL if minL != float('inf') else 0
