class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1
        idx = n-2
        while idx >= 0:
            if idx+ nums[idx] >= goal:
                goal = idx
            idx -= 1
        return goal==0   