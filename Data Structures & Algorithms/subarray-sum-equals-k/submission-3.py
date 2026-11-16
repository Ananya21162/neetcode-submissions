class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixCount = {0:1}
        prev = 0
        for num in nums:
            if num + prev - k in prefixCount:
                res += prefixCount[num + prev - k]
            prefixCount[num+prev] = prefixCount.get(num+prev,0)+1
            prev += num
        return res
