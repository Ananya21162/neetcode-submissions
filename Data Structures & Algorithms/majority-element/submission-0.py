class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = [0,0]
        freq_map = {}
        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i],0)+1
            if count[0] < freq_map[nums[i]]:
                count = [freq_map[nums[i]],nums[i]]
        return count[1]
        