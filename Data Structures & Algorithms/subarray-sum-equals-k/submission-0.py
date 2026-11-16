class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        sub = 0
        prefixSumMap = {0: 1}
        for num in nums:
            prefixSum += num
            if (prefixSum - k) in prefixSumMap:
                sub += prefixSumMap[prefixSum - k]
            if prefixSum in prefixSumMap:
                prefixSumMap[prefixSum] += 1
            else:
                prefixSumMap[prefixSum] = 1
        return sub