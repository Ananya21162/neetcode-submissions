class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxL = 0
        for idx, num in enumerate(nums):
            if num-1 in nums:
                continue
            else:
                count = 1
                while num+1 in nums:
                    count += 1
                    
                    num = num+1
                maxL = max(maxL,count)
        return maxL