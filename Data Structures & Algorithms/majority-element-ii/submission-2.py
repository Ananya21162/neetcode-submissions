class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqMap = {}
        maxC = len(nums)//3
        for num in nums:
            freqMap[num] = freqMap.get(num,0)+1
        ans = []
        for key, value in freqMap.items():
            if value > maxC:
                ans.append(key)
        return ans