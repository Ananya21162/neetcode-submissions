class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        i = len(nums)-1
        while i > 0:
            j,k = 0, 1
            while k <= i:
                if nums[j] > nums[k]:
                    # swap
                    nums[j], nums[k] = nums[k], nums[j]
                j += 1
                k += 1
            i -= 1
        return nums