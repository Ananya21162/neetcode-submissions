class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (l + r) // 2

            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1

        return -1