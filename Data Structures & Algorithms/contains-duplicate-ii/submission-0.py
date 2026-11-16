class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:    
        hash_nums = {}
        for i in range(len(nums)):
            if nums[i] in hash_nums:
                if abs(i-hash_nums[nums[i]]) <= k:
                    return True
            hash_nums[nums[i]] = i
        return False