class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        set_num = set(nums)
        for num in set_num:
            if num-1 in set_num:
                continue
            else:
                l = 1
                while (num + 1) in set_num:
                    l += 1
                    num += 1
                maxLen = max(maxLen,l)
        return maxLen



        