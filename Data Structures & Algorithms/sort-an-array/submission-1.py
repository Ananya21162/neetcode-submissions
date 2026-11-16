class Solution:
    def merge(self,nums,left,right,low,high):
        i,j = 0,0
        k = low
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        return nums[low:high+1]
    def sort(self,nums,low,high):
        if low == high:
            return nums[low:high+1]
        mid = (low + high) // 2
        left = self.sort(nums,low,mid)
        right = self.sort(nums,mid+1,high)
        return self.merge(nums,left,right,low,high)
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.sort(nums,0,len(nums)-1)