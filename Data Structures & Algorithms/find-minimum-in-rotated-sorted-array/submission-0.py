class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[l] <= nums[mid]: # left side is sorted
                ans= min(ans,nums[l])
                l = mid+1
            elif nums[mid] <= nums[r]:
                ans = min(ans,nums[mid])
                r = mid-1
        return ans
            
