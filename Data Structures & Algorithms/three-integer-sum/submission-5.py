class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if  i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            j, k = i + 1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])
               
                    j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k +1]:
                        k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else: 
                    j += 1
        return list(ans)