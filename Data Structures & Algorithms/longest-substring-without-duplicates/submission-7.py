class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_char = {}
        maxLen = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in hash_char:
                l = max(l,hash_char[s[r]]+1)
            maxLen = max(maxLen, r-l+1)
            hash_char[s[r]] = r
            r += 1
           
        return maxLen