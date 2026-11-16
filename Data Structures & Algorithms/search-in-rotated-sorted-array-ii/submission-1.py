class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[l] and nums[l] == nums[r]:
                l = l + 1
            elif nums[l] <= nums[mid]:
                if target >= nums[l] and nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if target> nums[mid] and nums[r] >= target:
                    l = mid+1
                else:
                    r = mid-1
         
        return False