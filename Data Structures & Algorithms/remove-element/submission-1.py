class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums)-1
        i = 0
        while i <= j:
            if nums[i] == val:
                while j > i:
                    if nums[j] != val:
                        break
                    else:
                        j = j-1
                if j == i:
                    return i
                # swap
                nums[i], nums[j] = nums[j], nums[i]
                j = j-1
            i += 1
            # print(nums)
        return i
            