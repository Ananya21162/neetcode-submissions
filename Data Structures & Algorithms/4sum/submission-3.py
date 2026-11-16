class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] > target:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if nums[i] + nums[j] > target:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                k, l = j+1, n-1
                while k < l:
                    value = nums[i] + nums[j] + nums[k] + nums[l]
                    if value == target:
                        ans.append([nums[i], nums[j] , nums[k] , nums[l]])
                        k += 1
                        l -= 1
                        while k < n and nums[k] == nums[k-1]:
                            k += 1
                    elif value > target:
                        l -= 1
                    else:
                        k += 1
        return ans